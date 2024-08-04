import os
from recommender import logger
from recommender.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status = True
            with open(self.config.status_file, 'w') as f:
                pass

            data = pd.read_csv(self.config.local_data_file)
            all_cols = list(data.columns)
            all_schema_keys = self.config.all_schema.keys()

            #for validating the data types
            size = len(all_schema_keys)
            count = 0
            for col in all_cols:
                count += 1
                for key in list(all_schema_keys):
                    if(col == key):
                        if(str(data.dtypes[col]) != (self.config.all_schema)[key]):
                            validation_status = False
                            logger.info(f"{col} type in dataset doesn't match with {key} in schema")
                            break
                if count == size:
                    pass
                else:
                    continue

            with open(self.config.status_file, 'a') as f:
                f.write(f"Type Validation status: {validation_status}")

                f.write("\n")

            #for validating the columns
            validation_status = True
            for col in all_cols:
                if col not in all_schema_keys:
                    validation_status = False
                    logger.info(f"{col} column doesn't match with the schema")
            
            with open(self.config.status_file, 'a') as f:
                f.write(f"Column Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            raise e