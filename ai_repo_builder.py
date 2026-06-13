import os
import time
import logging
from typing import List, Optional
from pydantic import BaseModel, Field
from google import genai
from github import Github, GithubException

# ==========================================
# 1. ENTERPRISE CONFIGURATION & LOGGING
# ==========================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("AI_Architect")

# ==========================================
# 2. ENHANCED AI DATA MODELS
# ==========================================
class RepositoryFile(BaseModel):
    file_path: str = Field(description="Complete path, e.g., 'src/main.py' or '.github/workflows/deploy.yml'")
    file_content: str = Field(description="The source code or configuration text.")
    is_ci_cd: bool = Field(description="True if this is a GitHub Actions or deployment file.")

class ProjectRepository(BaseModel):
    project_name: str = Field(description="Hyphen-separated name for the GitHub repository.")
    description: str = Field(description="Professional description of the project.")
    files: List[RepositoryFile] = Field(description="List of all files, including tests and CI/CD pipelines.")
    system_dependencies: List[str] = Field(description="List of system-level dependencies required.")

# ==========================================
# 3. ADVANCED GITHUB & AI MANAGER
# ==========================================
class EnterpriseAIGitHubBuilder:
    def __init__(self):
        gemini_key = os.environ.get("GEMINI_API_KEY")
        github_token = os.environ.get("GITHUB_TOKEN")
        
        if not gemini_key or not github_token:
            logger.error("Missing critical Environment Variables. Halting execution.")
            raise ValueError("GEMINI_API_KEY and GITHUB_TOKEN are required.")
            
        self.ai_client = genai.Client(api_key=gemini_key)
        self.gh_client = Github(github_token)
        self.user = self.gh_client.get_user()
        
    def generate_architecture(self, prompt: str) -> ProjectRepository:
        """Uses advanced LLM prompting to generate a full project, including CI/CD."""
        logger.info("Engaging AI to architect project based on user prompt...")
        
        system_instruction = (
            "You are a Staff-Level Software Architect. Your job is to generate a robust, "
            "production-ready repository. You MUST include:\n"
            "1. Source code following clean code principles.\n"
            "2. A comprehensive README.md.\n"
            "3. Docker configuration (Dockerfile/docker-compose.yml).\n"
            "4. A GitHub Actions pipeline (.github/workflows/main.yml) for testing.\n"
        )
        
        full_prompt = f"{system_instruction}\n\nClient Requirements: {prompt}"
        
        try:
            response = self.ai_client.models.generate_content(
                model='gemini-2.5-flash',
                contents=full_prompt,
                config={
                    'response_mime_type': 'application/json',
                    'response_schema': ProjectRepository,
                },
            )
            logger.info("AI architecture generation successful.")
            return response.parsed
        except Exception as e:
            logger.error(f"AI Generation Failed: {str(e)}")
            raise

    def deploy_with_pr_workflow(self, project: ProjectRepository):
        """Creates the repo, pushes to a dev branch, and opens a Pull Request."""
        logger.info(f"Initializing remote GitHub repository: {project.project_name}")
        
        try:
            repo = self.user.create_repo(
                name=project.project_name, 
                description=project.description,
                private=True, # Defaulting to private for enterprise safety
                auto_init=True 
            )
            logger.info(f"Repository created: {repo.html_url}")
        except GithubException as e:
            logger.error(f"GitHub Repo Creation Failed: {e.data.get('message')}")
            return
            
        time.sleep(3) # Wait for auto-init
        
        # 1. Create a Development Branch
        dev_branch_name = "feature/ai-initial-build"
        main_ref = repo.get_git_ref("heads/main")
        repo.create_git_ref(ref=f"refs/heads/{dev_branch_name}", sha=main_ref.object.sha)
        logger.info(f"Created development branch: {dev_branch_name}")
        
        # 2. Push files to the Development Branch
        for file in project.files:
            safe_path = file.file_path.lstrip('/')
            logger.info(f"Committing {safe_path}...")
            try:
                repo.create_file(
                    path=safe_path,
                    message=f"feat: AI generated {safe_path}",
                    content=file.file_content,
                    branch=dev_branch_name
                )
            except Exception as e:
                logger.warning(f"Could not commit {safe_path}: {e}")
                
        # 3. Create a Pull Request
        logger.info("Opening Pull Request to main branch...")
        try:
            pr = repo.create_pull(
                title="🚀 AI Architect: Initial Project Build",
                body="This PR contains the initial automated architecture generated by the AI agent.",
                head=dev_branch_name,
                base="main"
            )
            logger.info(f"✅ Pull Request successfully created: {pr.html_url}")
        except Exception as e:
            logger.error(f"Failed to create Pull Request: {e}")

# ==========================================
# 4. EXECUTION SCRIPT
# ==========================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print(" 🚀 ENTERPRISE AI GITHUB ARCHITECT ")
    print("="*50 + "\n")
    
    user_idea = input("Enter your project requirements:\n> ")
    
    try:
        builder = EnterpriseAIGitHubBuilder()
        project_data = builder.generate_architecture(user_idea)
        builder.deploy_with_pr_workflow(project_data)
        print("\n🎉 Deployment workflow completed successfully.")
    except Exception as e:
        print(f"\n❌ System failure: {e}")
