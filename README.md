<div align="center">

# 🚀 AI-Lastic-Repository 🧠
*Your Autonomous AI Software Engineer for GitHub*

</div>

---

## 📖 Overview

This script acts as your dedicated **AI engineer**. It utilizes the latest **Google GenAI API** to intellectually architect projects and write code, while seamlessly integrating with **PyGithub** to automatically construct the repository directly on your GitHub account.

> **💡 The Secret Sauce:** To ensure the AI’s output is professional, reliable, and completely free of formatting errors, this script leverages **Structured Outputs (`Pydantic`)**. This forces the AI's "mind" to output pure, structured data (precise file paths and raw code content), enabling the script to systematically push production-ready code to GitHub.

---

## ✨ Key Features

* 📝 **Advanced Logging:** Tracks every architectural decision and push operation professionally, replacing basic `print()` statements with enterprise-grade logs.
* 🔄 **Automated CI/CD Pipelines:** Automatically instructs the AI to generate complete GitHub Actions workflows for continuous integration.
* 🔀 **Smart Branch Management:** Safeguards your production environment by creating a dedicated `dev` branch and opening a structured **Pull Request** to `main`, rather than pushing directly.
* 🛡️ **Robust Error Handling:** Actively catches specific GitHub and API exceptions to ensure the script executes smoothly without unexpected crashes.

---

## 🛠️ Prerequisites

Before deploying your AI engineer, you need to install the required dependencies and configure your environment securely.

### 1️⃣ Install Dependencies
Run the following command in your terminal:
```bash
pip install google-genai pydantic pygithub
```
### **2️⃣ Obtain Your Access Tokens**
You will need two essential keys to grant the script its "brain" and its "hands":
- 🧠 GEMINI_API_KEY: Obtain this from Google AI Studio. This powers the AI generation.
- 🐙 GITHUB_TOKEN: Navigate to GitHub ➡️ Settings ➡️ Developer Settings ➡️ Personal Access Tokens (Classic). Generate a new token and ensure you check the repo scope to grant repository creation permissions.
## 🚀 How to Run It
Follow these steps to generate your first AI-built repository:
**Step 1:** Open your terminal.

**Step 2:**  Export your API keys temporarily so the script can access them securely.

- 🍏 Mac / 🐧 Linux:
- ```
  export GEMINI_API_KEY="your_api_key_here"
  export GITHUB_TOKEN="your_github_token_here"
  ```
- 🪟 Windows (Command Prompt):
- ```
  set GEMINI_API_KEY="your_api_key_here"
  set GITHUB_TOKEN="your_github_token_here"
  ```
**Step 3:** Execute the builder script.
```
python ai_repo_builder.py
```
**Step 4:** Provide your project prompt when asked.
### 📋 Example 1: Full-Stack Next.js & TypeScript Dashboard
#### Prompt to copy:
```
"Create a professional full-stack web application blueprint using Next.js (App Router) and TypeScript. The project should be an Administrative Dashboard featuring an analytics page, a user management table with mock data, and an integration with Tailwind CSS for styling. Include a comprehensive README.md with component documentation, a Dockerfile for containerized deployment, a .gitignore tailored for Next.js, and a GitHub Actions workflow that automatically runs ESLint and build checks on every push."
```
### 🌐 Example 2: Secure Node.js Express Microservice with Docker
#### Prompt to copy:
```
"Build a production-ready microservice using Node.js, Express, and JavaScript for an e-commerce Product Catalog API. The project must implement CRUD operations, structured logging using Winston, request validation using Joi, and error-handling middleware. Include a docker-compose.yml file that spins up the Node.js application along with a MongoDB database instance. Provide a professional README.md with clear API route specifications (endpoints, methods, request bodies), a .env.example file, and a GitHub Actions CI pipeline to run automated Jest tests."
```
**Step 5:** 🍿 Watch the magic! Sit back as the AI plans the architecture, initializes the repository on your GitHub account, and securely commits the code file by file.
