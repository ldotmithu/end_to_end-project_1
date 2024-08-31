import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')

project_name = "mlproject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "setup.py",
    "research/train.ipynb",
    "requirements.txt",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    if filedir:  # Check if the directory path is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created directory: {filedir} for the file: {filename}')

    if not file_path.exists():  # Check if the file does not exist
        file_path.touch()  # Create an empty file
        logging.info(f'Created file: {file_path}')
