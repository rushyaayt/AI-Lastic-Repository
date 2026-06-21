import os
from google import genai
from pydantic import BaseModel

class TestSuite(BaseModel):
    test_file_path: str
    test_code: str
    test_framework: str

def generate_tests(code_file: str, output_dir: str):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    with open(code_file, 'r') as f:
        code = f.read()
    
    # Generate tests using AI
    prompt = f"Generate comprehensive unit tests for this code:\n\n{code}"
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    # Save test file
    test_path = os.path.join(output_dir, f"test_{os.path.basename(code_file)}")
    with open(test_path, 'w') as f:
        f.write(response.text)
    
    print(f"✅ Tests generated: {test_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--output", default="tests/")
    args = parser.parse_args()
    
    generate_tests(args.file, args.output)
