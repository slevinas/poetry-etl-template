poetry-etl-template/
├── {{cookiecutter.project_slug}}/
│   ├── .gitignore
│   ├── Makefile
│   ├── pyproject.toml
│   ├── README.md
│   ├── main.py
│   ├── .pre-commit-config.yaml
│   ├── .env.example
│   ├── tests/
│   │   └── test_dummy.py
│   └── {{cookiecutter.project_slug}}/
│       └── __init__.py
├── hooks/
│   └── pre_gen_project.py
├── cookiecutter.json

# cookiecutter.json
{
  "project_name": "My ETL Project",
  "project_slug": "my_etl_project",
  "description": "A modern ETL project using Poetry",
  "author_name": "Your Name",
  "email": "you@example.com",
  "python_version": "3.11"
}

# Makefile contents

LDFLAGS := -L/opt/homebrew/opt/libffi/lib
CPPFLAGS := -I/opt/homebrew/opt/libffi/include
PKG_CONFIG_PATH := /opt/homebrew/opt/libffi/lib/pkgconfig

init:
	@echo "⚙️  Initializing Poetry project with local libffi paths..."
	LDFLAGS=$(LDFLAGS) \
	CPPFLAGS=$(CPPFLAGS) \
	PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) \
	poetry install || ( \
		echo "🔁 Installing cffi manually inside the virtual environment..."; \
		. .venv/bin/activate && \
		LDFLAGS=$(LDFLAGS) CPPFLAGS=$(CPPFLAGS) PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) \
		pip install --force-reinstall --no-cache-dir cffi && \
		poetry install \
	)
	- LDFLAGS=$(LDFLAGS) \
	CPPFLAGS=$(CPPFLAGS) \
	PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) \
	poetry run pre-commit install

git-init:
	git init
	poetry run pre-commit install

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

test:
	poetry run pytest

run:
	poetry run python main.py

# pyproject.toml
[tool.poetry]
name = "{{ cookiecutter.project_slug }}"
version = "0.1.0"
description = "{{ cookiecutter.description }}"
authors = ["{{ cookiecutter.author_name }} <{{ cookiecutter.email }}>"]
readme = "README.md"
packages = [{ include = "{{ cookiecutter.project_slug }}" }]

[tool.poetry.dependencies]
python = "^{{ cookiecutter.python_version }}"
pandas = "*"
requests = "*"
python-dotenv = "*"

[tool.poetry.group.dev.dependencies]
pytest = "*"
black = "*"
isort = "*"
ruff = "*"
pre-commit = "*"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

# .pre-commit-config.yaml
repos:
  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.4.4
    hooks:
      - id: ruff
        args: ["--fix"]
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace

# .gitignore
__pycache__/
*.pyc
.venv/
.env

# .env.example
# Sample environment variables
DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
API_KEY=your-api-key

# README.md
# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## 🚀 Project Setup

### 1. Create a project using this template:
```bash
cookiecutter ~/.cookiecutters/poetry-etl-template
```

### 2. Navigate to the new project folder:
```bash
cd <your_project_slug>
```

### 3. Initialize the project:
```bash
make init
```
This command:
- Runs `poetry install` with proper `libffi` flags.
- Automatically installs `cffi` if needed.
- Installs pre-commit hooks **if** the project is a Git repo.

❗ If `make init` fails with a Git-related error:
```bash
git init
make init  # Run it again now that Git is initialized
```

---

## 🛠 Common Commands

### Run your ETL script:
```bash
make run
```

### Lint and format code:
```bash
make lint
make format
```

### Run tests:
```bash
make test
```

### Add dependencies:
```bash
poetry add <package>
poetry add --group dev <package>
```

---

## 📁 Project Structure
```
project_slug/
├── .venv/                      # Poetry-managed virtualenv
├── main.py                    # ETL entrypoint
├── Makefile                   # Workflow automation
├── pyproject.toml             # Poetry config
├── .pre-commit-config.yaml    # Pre-commit hooks
├── .gitignore
├── .env.example               # Env template
├── tests/                     # Test suite
├── {{cookiecutter.project_slug}}/
│   └── __init__.py
```

# main.py
import os
from dotenv import load_dotenv
import pandas as pd
import requests

def extract():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()

def transform(data):
    return pd.DataFrame(data)

def load(df):
    print("Loaded data:")
    print(df.head())

def main():
    load_dotenv()
    data = extract()
    df = transform(data)
    load(df)

if __name__ == "__main__":
    main()

# tests/test_dummy.py
def test_dummy():
    assert 1 + 1 == 2

# hooks/pre_gen_project.py
def validate_slug(slug):
    import re
    if not re.match(r'^[_a-zA-Z][_a-zA-Z0-9]+$', slug):
        raise ValueError(
            f"Invalid project_slug '{slug}'. It must be a valid Python identifier."
        )

def main():
    import sys
    slug = '{{ cookiecutter.project_slug }}'
    try:
        validate_slug(slug)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

# {{cookiecutter.project_slug}}/__init__.py
# Optional package init

