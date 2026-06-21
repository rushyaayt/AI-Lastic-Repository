import os
from google import genai
from pathlib import Path

def generate_documentation(repo_path: str):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    # Scan Python files
    py_files = list(Path(repo_path).rglob("*.py"))
    
    documentation = "# 📚 Auto-Generated Documentation\n\n"
    
    for file in py_files:
        with open(file, 'r') as f:
            code = f.read()
        
        # Generate docs for each file
        prompt = f"Generate documentation for this Python file:\n\n{code}"
        
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        
        documentation += f"\n## {file.name}\n\n"
        documentation += response.text + "\n"
    
    # Save documentation
    with open(os.path.join(repo_path, "AUTO_DOCS.md"), 'w') as f:
        f.write(documentation)
    
    print("✅ Documentation generated: AUTO_DOCS.md")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    
    generate_documentation(args.repo)
