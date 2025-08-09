import os
from pathlib import Path

project_name = "aptos"

list_of_files = [
    # Core project files
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "dvc.yaml",
    "params.yaml",

    # --- NEW: Production-related files ---
    "Dockerfile",
    "docker-compose.yaml",
    
    # --- NEW: Application directory for serving ---
    f"app/__init__.py",
    f"app/main.py", # or app/api.py
    f"app/templates/index.html", # For the web UI
    f"app/static/style.css", # For styling the UI
    
    # --- END of NEW section ---

    # Notebooks and research
    "notebooks/exploratory.ipynb",
    "research/experiments.ipynb",
    
    # Source code structure
    "src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    
    # Directories for artifacts and logs
    "artifacts/.gitkeep",
    "saved_models/.gitkeep",
    "logs/.gitkeep",
    
    # Tests
    "tests/__init__.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    dirpath = filepath.parent

    if not dirpath.exists():
        dirpath.mkdir(parents=True, exist_ok=True)

    if not filepath.exists():
        filepath.touch()
        print(f"Created: {filepath}")
    else:
        print(f"Already exists: {filepath}")