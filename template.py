import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

package_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__py",
    f"src/{package_name}/components/__init__py",
    f"src/{package_name}/utils/__init__py",
    f"src/{package_name}/config/__init__py",
    f"src/{package_name}/pipeline/__init__py",
    f"src/{package_name}/entity/__init__py",
    f"src/{package_name}/constants/__init__py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for file {filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  #create an empty file
            logging.info(f"Creating directory: {filedir}")
    else:
        logging.info(f"{filename} already exist")