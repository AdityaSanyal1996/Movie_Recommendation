from recommender.config.configuration import ConfigurationManager
from recommender.components.Model_Inference import MovieRecommender
import joblib
from recommender import logger

STAGE_NAME = "Model Training/Inference stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model_training = MovieRecommender(config = model_training_config)
        model_training.similarities()
        similarities = model_training.similarity_df
        name = input("enter the name of the movie: ")
        movies = model_training.recommend(name)
        for i in movies:
            print(similarities.iloc[int(i), 1])

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e