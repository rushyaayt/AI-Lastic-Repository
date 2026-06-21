import os
import sys
import logging
import argparse
from typing import List
from pydantic import BaseModel, Field
from github import Github, GithubException
from google import genai
from google.genai import types

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- Pydantic Models for Structured GenAI Output ---
class FileChange(BaseModel):
    """Represents a single file to be created or modified."""
    file_path: str = Field(description="The exact relative path of the file in the repository.")
    file_content: str = Field(description="The complete, raw content of the file. Do not wrap in markdown code blocks.")
    commit_message: str = Field(description="A concise, conventional commit message for this change.")

class IssueResolution(BaseModel):
    """Structured output from the AI to resolve a GitHub issue."""
    branch_name: str = Field(description="A descriptive, kebab-case name for the new git branch (e.g., fix/issue-42-null-pointer).")
    pr_title: str = Field(description="A clear and descriptive title for the Pull Request.")
    pr_body: str = Field(description="A detailed markdown description for the PR explaining the fix and how it addresses the issue.")
    files_to_commit: List[FileChange] = Field(description="List of files to be added or modified to resolve the issue.")

# --- Core Functions ---
def setup_clients():
    """Initializes and returns Github and GenAI clients."""
    github_token = os.getenv("GITHUB_TOKEN")
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    
    if not github_token or not gemini_api_key:
        logging.error("Missing environment variables. Please set GITHUB_TOKEN and GEMINI_API_KEY.")
        sys.exit(1)
        
    g = Github(github_token)
    genai_client = genai.Client(api_key=gemini_api_key)
    return g, genai_client

def fetch_issue_context(g: Github, repo_name: str, issue_num: int) -> dict:
    """Fetches issue details using PyGithub."""
    try:
        repo = g.get_repo(repo_name)
        issue = repo.get_issue(issue_num)
        logging.info(f"Successfully fetched Issue #{issue_num}: {issue.title}")
        
        return {
            "title": issue.title,
            "body": issue.body or "No description provided.",
            "labels": [label.name for label in issue.labels],
            "comments": [comment.body for comment in issue.get_comments()][:3] # Limit to last 3 comments for context window
        }
    except GithubException as e:
        logging.error(f"Failed to fetch issue: {e}")
        sys.exit(1)

def generate_fix_with_genai(client: genai.Client, issue_context: dict) -> IssueResolution:
    """Uses Google GenAI to generate a structured resolution for the issue."""
    prompt = f"""
    You are an elite autonomous software engineer. Your task is to resolve the following GitHub issue.
    
    Issue Title: {issue_context['title']}
    Issue Description: {issue_context['body']}
    Labels: {', '.join(issue_context['labels'])}
    Recent Comments: {'\n---\n'.join(issue_context['comments'])}
    
    Analyze the issue deeply. Determine the root cause and the most elegant, production-ready solution.
    Provide the exact code changes required. 
    
    IMPORTANT: 
    - Ensure all code is fully implemented (no placeholders like "// rest of code here").
    - Output strictly valid JSON matching the provided Pydantic schema.
    - Do NOT wrap file_content in markdown code blocks (```python ... ```). Just raw text.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", # Using a fast, capable model
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=IssueResolution,
            )
        )
        logging.info("GenAI successfully generated a structured resolution.")
        return response.parsed
    except Exception as e:
        logging.error(f"GenAI generation failed: {e}")
        sys.exit(1)

def apply_fix_and_create_pr(g: Github, repo_name: str, resolution: IssueResolution, issue_num: int):
    """Creates a branch, commits files, and opens a PR using PyGithub."""
    repo = g.get_repo(repo_name)
    default_branch = repo.default_branch
    
    # 1. Create a new branch
    try:
        sb = repo.get_branch(default_branch)
        base_sha = sb.commit.sha
        repo.create_git_ref(ref=f"refs/heads/{resolution.branch_name}", sha=base_sha)
        logging.info(f"Created new branch: {resolution.branch_name}")
    except GithubException as e:
        logging.warning(f"Branch creation note: {e.data.get('message', 'Unknown error')}")
        
    # 2. Commit the generated files
    for file_change in resolution.files_to_commit:
        try:
            # Check if file exists to decide between create or update
            contents = repo.get_contents(file_change.file_path, ref=resolution.branch_name)
            repo.update_file(
                path=file_change.file_path,
                message=file_change.commit_message,
                content=file_change.file_content,
                sha=contents.sha,
                branch=resolution.branch_name
            )
            logging.info(f"Updated existing file: {file_change.file_path}")
        except GithubException:
            # File doesn't exist, create it
            repo.create_file(
                path=file_change.file_path,
                message=file_change.commit_message,
                content=file_change.file_content,
                branch=resolution.branch_name
            )
            logging.info(f"Created new file: {file_change.file_path}")
            
    # 3. Open the Pull Request
    pr_body = f"{resolution.pr_body}\n\n---\n🤖 *This PR was automatically generated by AI-Lastic-Repository to resolve #{issue_num}.*\n\nCloses #{issue_num}"
    pr = repo.create_pull(
        title=resolution.pr_title,
        body=pr_body,
        head=resolution.branch_name,
        base=default_branch
    )
    logging.info(f"🎉 Successfully created PR: {pr.html_url}")

def main():
    parser = argparse.ArgumentParser(description="AI Issue Resolver - Automatically fixes GitHub issues and opens PRs.")
    parser.add_argument("--repo", required=True, help="The GitHub repository (e.g., 'username/repo-name')")
    parser.add_argument("--issue", type=int, required=True, help="The issue number to resolve")
    args = parser.parse_args()

    g, genai_client = setup_clients()
    
    logging.info(f"Starting resolution process for Issue #{args.issue} in {args.repo}...")
    context = fetch_issue_context(g, args.repo, args.issue)
    
    resolution = generate_fix_with_genai(genai_client, context)
    
    apply_fix_and_create_pr(g, args.repo, resolution, args.issue)

if __name__ == "__main__":
    main()
