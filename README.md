Here is the fully converted, highly professional `README.md`. It combines the centered header you requested, the exact structural style of your example (Overview, Secret Sauce, Key Features, OS-specific commands), and the new `.env` setup and dual-script functionality.

Just click the **Copy** button in the top right corner of the box below, paste it into your `README.md`, and push it to GitHub!


<div align="center">

# 🤖 AI-Lastic-Repository

**AI-Lastic-Repository** is an autonomous AI software engineer powered by **Google GenAI**, **Pydantic**, and **PyGithub**. It doesn't just write code; it interacts directly with your GitHub repositories to build projects from scratch and automatically resolve open issues.

</div>

---

## 📖 Overview

This repository acts as your dedicated **AI engineering team**. It utilizes the latest **Google GenAI API** to intellectually architect projects, write production-ready code, and seamlessly integrate with **PyGithub** to automatically construct repositories or resolve open issues directly on your GitHub account.

> **💡 The Secret Sauce:** To ensure the AI’s output is professional, reliable, and completely free of formatting errors, these scripts leverage **Structured Outputs (`Pydantic`)**. This forces the AI's "mind" to output pure, structured data (precise file paths and raw code content), enabling the scripts to systematically push flawless code to GitHub without parsing messy markdown.

---

## ✨ Key Features

* 🏗️ **Dual Autonomous Scripts:** Includes `ai_repo_builder.py` to generate entire repositories from scratch, and `ai_issue_resolver.py` to automatically fix open GitHub issues and open Pull Requests.
* 🧠 **Strict Pydantic Enforcement:** Forces the LLM to output pure JSON mapped to Python data models, ensuring 100% reliable file paths, commit messages, and code blocks.
* 🔀 **Smart Branch & PR Management:** Safeguards your production environment by creating dedicated branches (e.g., `fix/issue-42`) and opening structured Pull Requests rather than pushing directly to `main`.
* 🛡️ **Robust Error Handling:** Actively catches specific GitHub and API exceptions, intelligently checking if files exist before updating or creating them to prevent API crashes.
* 📝 **Enterprise-Grade Logging:** Tracks every architectural decision, API call, and push operation professionally, replacing basic `print()` statements with detailed, timestamped logs.

---

## 🛠️ Prerequisites

Before deploying your AI engineers, you need to install the required dependencies and configure your environment securely.

### 1️⃣ Install Dependencies
Run the following command in your terminal:
```bash
pip install google-genai pydantic pygithub python-dotenv
```

### 2️⃣ Obtain Your Access Tokens
You will need two essential keys to grant the scripts their "brain" and their "hands":
- 🧠 **GEMINI_API_KEY:** Obtain this from [Google AI Studio](https://aistudio.google.com/). This powers the AI generation.
- 🐙 **GITHUB_TOKEN:** Navigate to GitHub ➡️ Settings ➡️ Developer Settings ➡️ Personal Access Tokens (Classic). Generate a new token and **ensure you check the `repo` scope** to grant repository creation and PR permissions.

### 3️⃣ Secure Environment Setup
 Grab your own tokens and API
```env
# .env file
GITHUB_TOKEN=ghp_paste_your_github_token_here
GEMINI_API_KEY=AIza_paste_your_gemini_key_here
```


---

## 🚀 How to Run It

Follow these steps to deploy your AI engineers.

**Step 1:** Open your terminal and navigate to the project directory.

**Step 2:** The scripts will automatically read your keys from the `.env` file. If you prefer not to use a `.env` file, you can export them temporarily:

- 🍏 Mac / 🐧 Linux:
  ```bash
  export GEMINI_API_KEY="your_api_key_here"
  export GITHUB_TOKEN="your_github_token_here"
  ```
- 🪟 Windows (Command Prompt):
  ```cmd
  set GEMINI_API_KEY="your_api_key_here"
  set GITHUB_TOKEN="your_github_token_here"
  ```

**Step 3:** Execute your desired script.

### 📋 Example 1: Build a New Repository from Scratch
Use the repo builder to generate a brand new project.
```bash
python ai_repo_builder.py --prompt "Your prompt here" --repo-name "my-new-repo"
```

#### Prompt to copy:
```text
"Create a professional full-stack web application blueprint using Next.js (App Router) and TypeScript. The project should be an Administrative Dashboard featuring an analytics page, a user management table with mock data, and an integration with Tailwind CSS for styling. Include a comprehensive README.md, a Dockerfile for containerized deployment, and a GitHub Actions workflow that automatically runs ESLint and build checks on every push."
```

### 🌐 Example 2: Automatically Resolve a GitHub Issue
Use the issue resolver to fix a bug or add a feature to an existing repository.
```bash
python ai_issue_resolver.py --repo "your-username/your-repo-name" --issue 42
```
*Replace `42` with the actual issue number. The script will automatically create a branch (e.g., `fix/issue-42`), commit the fix, and open a Pull Request!*

#### Context to provide:
Simply ensure the GitHub issue has a clear title and description. The AI will read the issue context, including labels and recent comments, to formulate the perfect fix.

**Step 4:** 🍿 **Watch the magic!** Sit back as the AI plans the architecture, writes the code, and securely commits it to your GitHub account.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/rushyaayt/AI-Lastic-Repository/issues). 

*💡 Pro Tip: Try using `ai_issue_resolver.py` to fix them automatically!*

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
```
