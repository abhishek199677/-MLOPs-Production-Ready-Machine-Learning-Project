import os
from pathlib import Path

project_name = "us_visa"     #partent folder name

list_of_files = [

    f"{project_name}/__init__.py",    #constructor file for components folder
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",      #constructor file for configuraton folder
    f"{project_name}/constants/__init__.py",          #constructor file for constants folder
    f"{project_name}/entity/__init__.py",             #constructor file for entity folder
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",           #constructor file for exception folder
    f"{project_name}/logger/__init__.py",              #constructor file for logger folder
    f"{project_name}/pipline/__init__.py",             #constructor file for pipline folder
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",                #constructuir file for utils folder
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]



for filepath in list_of_files:      #iterating through each file 
    filepath = Path(filepath)        
    filedir, filename = os.path.split(filepath)  
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")