import os
from pathlib import Path

def setup_environment():
    print("🚀 AI-Lastic Repository Setup Wizard\n")
    
    # Get GitHub Token
    github_token = input("Enter your GitHub Token: ").strip()
    
    # Get Gemini API Key
    gemini_key = input("Enter your Gemini API Key: ").strip()
    
    # Create .env file
    env_content = f"""GITHUB_TOKEN={github_token}
GEMINI_API_KEY={gemini_key}
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    # Create .gitignore if not exists
    if not Path('.gitignore').exists():
        with open('.gitignore', 'w') as f:
            f.write(".env\n__pycache__/\n*.pyc\n")
    
    print("\n✅ Setup complete! Your .env file has been created.")
    print("⚠️  Remember: Never commit .env to GitHub!")

if __name__ == "__main__":
    setup_environment()
