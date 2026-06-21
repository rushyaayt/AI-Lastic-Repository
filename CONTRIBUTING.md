# Contributing to AI-Lastic-Repository

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Setup

```bash
git clone https://github.com/rushyaayt/AI-Lastic-Repository.git
cd AI-Lastic-Repository
pip install -r script/requirements.txt
script/setup_env.py

```

## Code Style

- Use Black for formatting
- Follow PEP 8 guidelines
- Add docstrings to all functions
- Write tests for new features

## Testing

```bash
pytest tests/
```


### **`setup.py`** (Root directory - for easy installation)

```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("script/requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-lastic-repository",
    version="1.0.0",
    author="rushyaayt",
    description="Autonomous AI Software Engineer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ai-build=script.ai_repo_builder:main",
            "ai-fix=script.ai_issue_resolver:main",
        ],
    },
)
```

---
