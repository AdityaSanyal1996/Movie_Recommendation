import os
from box.exceptions import BoxValueError
import yaml
from recommender import logger
from box import ConfigBox
from pathlib import Path


def read_yaml(path_to_file: Path) -> ConfigBox: 
    '''we need to put a yaml file in a python data structure to be able to parse it, 
    ConfigBox object helps work with yaml files easily
    
    args: "Path" object to the path of the file
    returns: "ConfigBox" object of the yaml dictionaries
    
    '''
    try:
        with open(path_to_file) as f:
            file = yaml.safe_load(f)
            logger.info(f"yaml file:{path_to_file} loaded successfully")
            return ConfigBox(file)
    except BoxValueError:
        filename = (os.path.split())[1]
        logger.info(f"yaml file:{filename} cannot be empty")
        raise Exception("yaml file is empty")
    except Exception as e:
        raise e
    


def create_directories(directories:list, verbose = True):
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"create directory at {directory}")


def get_size(path:Path)->str:
    size_in_kb = os.path.getsize(path)/1024
    return f"~{size_in_kb:.2f} KB"