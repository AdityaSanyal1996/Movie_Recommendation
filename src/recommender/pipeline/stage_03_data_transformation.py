from recommender.config.configuration import ConfigurationManager
from recommender.components.Data_Transformation import DataTransformation
from recommender import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformatin_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformatin_config)
        data_transformation.transform_data()

# we have written the same code in main.py and don't want this code to get executed again
# during import from this module, therefore we have added the if __name__ == '__main__':
if __name__ == '__main__':  
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e