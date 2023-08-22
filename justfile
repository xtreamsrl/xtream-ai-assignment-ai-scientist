set shell := ["zsh", "-uc"]
set positional-arguments

# List all available recipes
help:
  @just --list

# Create a git repo if not exists, install dependencies and pre-commit hooks
install:
  @{{just_executable()}} needs pdm

  pdm install --dev
  pdm run pre-commit install --install-hooks

# Update dependencies and update pre-commit hooks
update:
  pdm sync
  pdm update
  pdm run pre-commit install-hooks
  pdm run pre-commit autoupdate

# Launch a jupyter lab instance
@lab:
  pdm run jupyter-lab

# Format code with black and isort
@fmt:
  pdm run black -- src tests
  pdm run blacken-docs -- src/**/*.py tests/*.py
  pdm run ruff --select=I001 --fix -- src tests

# Lint the project with Ruff
@lint:
  pdm run ruff -- src tests

# Perform static type checking with mypy
@typecheck:
  pdm run mypy -- src tests

# Audit dependencies with pip-audit
@audit:
  pdm run pip-audit
  pdm run deptry -- src

# Assert a command is available
[private]
needs *commands:
  #!/usr/bin/env zsh
  set -euo pipefail
  for cmd in "$@"; do
    if ! command -v $cmd &> /dev/null; then
      echo "$cmd binary not found. Did you forget to install it?"
      exit 1
    fi
  done

# Export the python kernel to run code inside Jupyter
export-kernel destination="$HOME/.local":
  pdm run python -m ipykernel install --name=xtream-ai-assignment --display-name="xtream AI assignment" --prefix={{destination}}
