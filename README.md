# AI-Lastic-Repository
This script acts as your AI engineer. It uses the latest Google GenAI API to intellectually build the project architecture and write the code, and it uses PyGithub to automatically construct the repository on your GitHub account.

To make the AI’s output "professional and good" without failing or outputting broken formatting, this script leverages Structured Outputs (Pydantic). This forces the AI's mind to output pure data (file paths and code content) that the script can systematically push to GitHub.
## Prerequisites
Before running the script, you need to install the required libraries and set up two API keys.
#### 1. Install the libraries via your terminal:
```
pip install google-genai pydantic pygithub
```
#### 2. Get your Tokens:
- **GEMINI_API_KEY:** Get this from Google AI Studio. This gives the script its "brain."
- **GITHUB_TOKEN:** Go to GitHub -> Settings -> Developer Settings -> Personal Access Tokens (Classic). Generate a token and check the repo box so it has permission to create repositories.


## How to Run It
1. Open your terminal.
2. Set your API keys temporarily so the script can read them:
 - **Mac/Linux:** export GEMINI_API_KEY="your_api_key_here" and export GITHUB_TOKEN="your_github_token_here"
 - **Windows (Command Prompt):** set GEMINI_API_KEY="your_api_key_here" and set GITHUB_TOKEN="your_github_token_here"
3. Run the script: python ai_repo_builder.py
4. Type in your prompt (e.g., "Build a professional modern REST API using FastAPI with a user login system, a PostgreSQL database connection setup, and a beautiful README file.").
5. Watch the terminal as the AI plans the files, creates the repo on your GitHub account, and commits the code file by file.
   
