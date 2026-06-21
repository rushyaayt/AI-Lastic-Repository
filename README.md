<div align="center">
# 🤖 AI-Lastic-Repository

**AI-Lastic-Repository** is an autonomous AI software engineer powered by **Google GenAI**, **Pydantic**, and **PyGithub**. It doesn't just write code; it interacts directly with your GitHub repositories to build projects from scratch and automatically resolve open issues.

</div>

---


## ✨ Features

This repository contains two powerful autonomous scripts:

1. **`ai_repo_builder.py` (Rushikesh)**
   - Generates entire GitHub repositories from scratch based on a simple prompt.
   - Structures folders, writes production-ready code, and pushes the initial commit.

2. **`ai_issue_resolver.py` (Rushikesh)** 
   - Reads open GitHub Issues in your repository.
   - Analyzes the issue context and uses GenAI to write the exact code needed to fix it.
   - Automatically creates a new branch, commits the files, and opens a Pull Request (PR) to resolve the issue.

---

## 🛠️ Prerequisites

- Python 3.9 or higher
- A GitHub account
- A Google AI Studio account (for the Gemini API)

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/rushyaayt/AI-Lastic-Repository.git
   cd AI-Lastic-Repository
   ```
   
2. Install the required Python packages:
   ```bash
   pip install google-genai PyGithub pydantic python-dotenv
   ```

---

## 🔐 Environment Setup (Crucial)

To allow the scripts to interact with GitHub and Google GenAI, you must set up your API keys securely using a `.env` file.

### Step 1: Get your API Keys
1. **GitHub Token:** 
   - Go to GitHub **Settings** > **Developer settings** > **Personal access tokens** > **Tokens (classic)**.
   - Generate a new token. **Important:** You must check the **`repo`** scope so the script can create branches and open PRs.
2. **Gemini API Key:**
   - Go to [Google AI Studio](https://aistudio.google.com/).
   - Click **Get API key** and create a new key.

### Step 2: Create the `.env` file
In the root directory of this project, create a file named exactly `.env` and add your keys:

```env
# .env file
GITHUB_TOKEN=ghp_paste_your_github_token_here
GEMINI_API_KEY=AIza_paste_your_gemini_key_here
```

### Step 3: Protect your keys
**Never commit your `.env` file to GitHub!** Ensure your `.gitignore` file includes `.env`:

```gitignore
# .gitignore
.env
__pycache__/
*.pyc
```

---

## 🚀 Usage

### 1. Build a New Repository from Scratch
Use the repo builder to generate a brand new project.

```bash
python ai_repo_builder.py --prompt "Build a Python FastAPI backend for a todo list app with SQLite" --repo-name "my-new-todo-app"
```

### 2. Automatically Resolve a GitHub Issue
Use the issue resolver to fix a bug or add a feature to an existing repository.

```bash
python ai_issue_resolver.py --repo "your-username/your-repo-name" --issue 42
```
*Replace `42` with the actual issue number you want the AI to fix. The script will automatically create a branch (e.g., `fix/issue-42`) and open a Pull Request!*

---

## 🧠 How it Works

Both scripts utilize **Pydantic** to enforce strict structured outputs from the LLM. Instead of asking the AI to "write code" and parsing messy markdown, we force the AI to output pure JSON that maps directly to our Python data models. This ensures:
- No hallucinated markdown formatting breaking the code.
- Reliable file paths and commit messages.
- Seamless integration with the GitHub API via PyGithub.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/rushyaayt/AI-Lastic-Repository/issues). 

*Tip: Try using `ai_issue_resolver.py` to fix them!*

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
```

### Next Steps:
1. Click the **Copy** button on the top right of the code block above.
2. Open your `README.md` file in your repository.
3. Delete the old content, paste the new content, and save.
4. Commit and push to GitHub! 

