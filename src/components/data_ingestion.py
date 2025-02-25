from dataclasses import dataclass
from pathlib import Path
from src.utils import read_yaml, create_directories
from src.logging import logger
from src.exception import Customexception
from src.constants import *
import sys


@dataclass
class dataingestionconfig:
    root_dir: Path
    source_url: Path
    local_data_file: Path
    unzip_dir: Path
    
    
class dataingestion:
    def __init__(self,config_path=CONFIG_FILE_PATH,params_path=PARAMS_FILE_PATH):
        try:
            self.config = read_yaml(config_path)
            self.params = read_yaml(params_path)
            
            create_directories(self.config.artifacts_root)
        except Exception as e:
            raise Customexception(e,sys)    
        
            
















