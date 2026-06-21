import os
from github import Github
from google import genai
from pydantic import BaseModel
from typing import List

class CodeReview(BaseModel):
    file_path: str
    line_number: int
    severity: str  # "critical", "warning", "suggestion"
    message: str
    suggestion: str

def review_pull_request(repo_name: str, pr_number: int):
    g = Github(os.getenv("GITHUB_TOKEN"))
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    # Get changed files
    files = pr.get_files()
    
    for file in files:
        if file.patch:
            # Send to AI for review
            review = analyze_code(file.patch, client)
            if review:
                pr.create_review_comment(
                    body=f"🤖 AI Suggestion: {review.suggestion}",
                    commit=pr.head.sha,
                    path=file.filename,
                    position=review.line_number
                )

def analyze_code(patch: str, client):
    # AI analysis logic here
    pass

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--pr", type=int, required=True)
    args = parser.parse_args()
    
    review_pull_request(args.repo, args.pr)
