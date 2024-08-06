import pandas as pd
from recommender import logger
from recommender.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_data(self):
            try:
                dataset = pd.read_csv(self.config.local_data_file)
                df = dataset[['type', 'title', 'description']].copy()
                df.to_csv(self.config.transformed_data_file, index = False)
                logger.info(f"transformed data stored in {self.config.transformed_data_file}")
            except Exception as e:
                raise e