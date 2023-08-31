 #the pupose of this utils is to make a common space where all frequently used functions reside. 
 # Therefore, whenever we want we can use them by simply importing them. 
 
import os
from box.exceptions import BoxValueError
import yaml
from end_to_end_mlops import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
 
 
 # Basic Functionalities
 
@ensure_annotations 
def read_yaml(path_to_yaml_file: Path) -> ConfigBox:
    '''reads yaml file 
    
    Args:
        path_to_yaml_file (str) : file path
        
    Raises: 
    
        ValueError: if yaml file is empty
        Exception e
    Returns: 
        ConfigBox: 
        
    
    '''
    
    try: 
        with open(path_to_yaml_file) as yaml_file:
            file_content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file : {path_to_yaml_file} read successfully")
            return ConfigBox(file_content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_dicts: list, verbose=True):
    '''This creates list of directories from given list
    
    Args: 
        path_to_dicts (list): list of the paths of directories 
    
    '''
    
    for path in path_to_dicts:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
            
@ensure_annotations
def save_json(path:Path,data:dict):
    ''' save the json data 
    
    Args: 
        path(Path) : path to json file
        data(dict) : data to be saved in json file 
        
    
    
    '''
    
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
        
    logger.info(f"Json file successfully saved at: {path}")
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    '''
    loads the json file data 
    
    Args:
        path(Path) : path to json file
    
    Returns:
        ConfigBox
    '''
    
    with open(path) as f:
        data = json.load(f)
        
    logger.info(f"Json file loaded successfully from: {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data: Any, path:Path):
    ''' saves the content in binary file
    
    Args: 
        data(Any) : data to be saved as binary
        path(Path) : path to binary file
        
    '''
    
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file successfully saved at: {path}")
    
    
    
@ensure_annotations
def load_bin(path:Path) -> Any:
    '''
    load the binary file
    
    Args:
        path(Path) : path of the binary file
        
    Returns:
        Any:
    '''
    
    
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    
    '''
    get the size in KB
    
    Args:
        path(Path) : path of the file
        
    Returns : 
        str: size in KB
    
    '''
    
    
    size = round(os.path.getsize(path)/1024)
    return f"~ {size} KB"

