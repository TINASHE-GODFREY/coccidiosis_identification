# In this module, I am  writing functions that are commonly used the the programme
import os
from box.exceptions import BoxValueError
import yaml 
from classifier import logger
import json 
import joblib
from ensure import ensure_annotations
from box import Config_Box 
from  pathlib import Path
from typing import Any 
import base64 


#decorator 
@ensure_annotations

#function to read yaml files 
def read_yaml(path_to_yaml: Path) -> Config_Box:
    """ reads yaml file and returns

    Args:
        path_to_yaml(str): path like input
    
    Raises:
        ValueError: if yaml is empty
    
    Returns:
    Config_Box: Config_Box type

"""

    # code to handle excptions if anything does wrong with reading the yaml file
    try:
       with open(path_to_yaml) as yaml_file:
           content= yaml.safe_load(yaml_file)
           logger.info(f"yaml file: {path_to_yaml} loaded succefully")
           return Config_Box(content)
   

    except BoxValueError:
       raise ValueError("yaml file is empty")
    except Exception as e:
       raise e





# function to create directories 
@ensure_annotations
def create_dirctories(path_to_directories: list, verbase=True):
   """create a list of directories 

   Args:
       path_to_directories(list):list of path of path_to_directories
       ignore_log(bool, optional): ignore if multiple dirs is to be created. Defaults to Flase
   """
   for path in path_to_directories:
      os.makedirs(path, exist_ok=True)
      if verbase:
         logger.info(f"created a directory at: {path}")





#function to load the json file
@ensure_annotations
def load_json(path: Path) -> Config_Box:
   """load json file 

   Args:
       path (Path): path to json file 
   Returns:
       Config_Box: data as  class attributes instead of dict

   """
   with  open(path) as f:
      content=json.read(f)

   logger.info(f"json file is loaded from {path}")
   return Config_Box(content)




# fuction that saves 
@ensure_annotations
def save_json(path: Path, data: dict):
   """save json data

   Args:
       path(Path): path to json file 
       data (dict): data to be saved in the json file
    """
   
   with open(path, "w") as f:
      json.dump(data, f, indent=4)
   logger.info(f" json file saved at:{path}")
   




#function to load the binary file
@ensure_annotations
def load_bin(path: Path) -> Any:
   """load the binary file 

   Args:
       path(Path): path to the binary file 
   
   Ruturns:
       Any: object stored in the file

    """
   data=joblib.load(path)
   logger.info(f"binary file loaded from: {path}")
   return data





# function to save in form of binary  
@ensure_annotations

def save_binary(data: Any, path:Path):
   """save binary file 

   Args:
       data(Any): data to be saved as binary 
       path(Path): path to the binary file 
    """
   
   joblib.dump(value=data, filename=path)
   logger.info(f"binary file saved at: {path}")



#function to  chect the size of any file or folder
@ensure_annotations

def get_size(path: Path) -> str:
   """get the size in KB 
   
   Args:
       path(Path): path to the file 
   Returns:
       str: size in KB
    """
   size_in_kb= round(os.path.getsize(path)/1024)
   return f"~ {size_in_kb} KB "



#function to encode an image into base64
def encodeImageIntoBase64(croppedImagePath):
   with open(croppedImagePath, "rb")as f:
      return base64.b64encode(f.read())
   

#function to decode an image 
def decodeImage(img_string, filename):
   image_data=base64.b64decode(img_string)
   with open(filename, "wb") as f:
      f.write(image_data)
      f.close() 



    






   
 



   




   
