# poetry-etl-template

A modern, customizable ETL project scaffold for Python using [Poetry](https://python-poetry.org/), pre-configured with linting, testing, and environment automation.

---

## ✅ Features

- 📦 Poetry for dependency & virtualenv management
- 🧪 Pytest for testing
- 🎯 Pre-commit hooks: `ruff`, YAML checks, and more
- 🧹 Linting with `black`, `isort`, and `ruff`
- 🛠 Makefile automation for common tasks
- 🔒 .env + example support
- ✅ Git hook bootstrap built-in

---

## 🚀 Quickstart

### 1. Generate a project:
```bash
cookiecutter ~/.cookiecutters/poetry-etl-template
```

### 2. Navigate to your project:
```bash
cd <your_project_slug>
```

### 3. Initialize the environment:
```bash
make init
```
If pre-commit fails with a Git error:
```bash
git init
make init
```

---

## 🧰 Common Make Targets

| Command        | Description                         |
|----------------|-------------------------------------|
| `make run`     | Run the ETL pipeline                |
| `make lint`    | Run Ruff linter                     |
| `make format`  | Auto-format using Ruff              |
| `make test`    | Run pytest test suite               |
| `make init`    | Install deps + pre-commit setup     |

---

## 📁 Template Structure

```
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
```

---

## 🧵 Suggested GitHub Topics

- `cookiecutter`
- `poetry`
- `etl`
- `template`
- `python`
- `data-engineering`
- `scaffold`

---

## 🌐 Publishing to GitHub

```bash
cd ~/.cookiecutters/poetry-etl-template

git init
# Create a repo on GitHub: https://github.com/new

# Replace 'your-username'
git remote add origin git@github.com:your-username/poetry-etl-template.git
git add .
git commit -m "Initial commit: Poetry ETL Cookiecutter Template"
git branch -M main
git push -u origin main
```

---

Made with ❤️ to simplify your Python ETL project bootstrapping 🚀

