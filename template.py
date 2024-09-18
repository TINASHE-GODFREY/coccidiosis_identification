import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,  format="[%(ascitime)s] : %(message)s:")

project_name= "classifier"

list_of_folders=[
    
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componets/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py", # might coause an error here
    f"src/{project_name}/pipeline/configuration.py/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "parameters.yaml",
    "requrements.txt",
    "setup.py",
    "research/trials.ipynb"  

]

for file_path in list_of_folders:
        file_path= Path(file_path)
        file_dir, file_name= os.path.split(file_path)

        if file_dir != "":
                os.makedirs(file_dir, exist_ok=True)
                logging.info(f"creating a directory {file_dir} for the file {file_name}")


        if ( not os.path.exists(file_path) or os.path.getsize(file_path==0)):
                with open(file_path, "w") as f:
                        pass
                        logging.info(f"creating a new file: {file_path}")   
        else:
                logging.info(f"{file_name} already exits")
                
