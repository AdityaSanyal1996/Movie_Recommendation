import os
from recommender import logger
from recommender.entity.config_entity import DataIngestionConfig
from pathlib import Path
import shutil
from recommender.utils.common import get_size

import os
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def load_dataset(self):
        if not os.path.exists(self.config.local_data_file):
            file_path = 'dataset/netflix_dataset.csv'
            os.makedirs(self.config.root_dir, exist_ok=True)
            shutil.copyfile(Path(file_path), self.config.local_data_file)
            logger.info(f"dataset {os.path.basename(file_path)} loaded successfully")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        