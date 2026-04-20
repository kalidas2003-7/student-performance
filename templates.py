import os
from pathlib import Path

# Files relative to current root directory
list_of_files = [
    "src/__init__.py",
    "src/config.py",

    "src/components/__init__.py",
    "src/pipelines/__init__.py",
    "src/utils/__init__.py",

    "tests/__init__.py",

    "notebooks/.gitkeep",
    "logs/.gitkeep",
    "artifacts/.gitkeep",

    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
    "main.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create file only if it doesn't exist
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass

# ---- Add default content safely ---- #

def write_if_empty(path, content):
    path = Path(path)
    if path.stat().st_size == 0:
        with open(path, "w") as f:
            f.write(content)

# requirements.txt
write_if_empty("requirements.txt", """pandas
numpy
scikit-learn
matplotlib
seaborn
torch
tensorflow
""")

# setup.py
write_if_empty("setup.py", """
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
)
""")

# README.md
write_if_empty("README.md", "# Project Title\n\nDescription here.")

# .gitignore
write_if_empty(".gitignore", """
__pycache__/
*.pyc
*.pyo
.env
venv/
.ipynb_checkpoints/
logs/
artifacts/
""")

# main.py
write_if_empty("main.py", """
def main():
    print("Project started...")

if __name__ == "__main__":
    main()
""")

print("✅ Structure initialized in current project root!")
