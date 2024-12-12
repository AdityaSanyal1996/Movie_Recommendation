from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from recommender import logger
import os
from pathlib import Path
import joblib
from recommender.entity.config_entity import ModelTrainingConfig


class MovieRecommender:
    def __init__(self, config:ModelTrainingConfig):
        self.config = config
    
    def similarities(self):
        df = pd.read_csv(self.config.transformed_data_file)
        vectorizer = TfidfVectorizer(stop_words='english')
        description_matrix = vectorizer.fit_transform(df['description'])
        description_matrix.toarray()
        cosine_similarities = cosine_similarity(description_matrix)
        cosine_similarities = pd.DataFrame(cosine_similarities)
        self.similarity_df = df[['type', 'title']].copy()
        self.similarity_df = pd.concat([self.similarity_df, cosine_similarities], axis=1)
        self.similarity_df.to_csv(self.config.tokenized_data)
        logger.info(f"created and saved the similarity matrix succesfully!")
    
    def recommend(self, name:str):
        movie = self.similarity_df[self.similarity_df['title'] == name].iloc[:, 2:]
        movie_index = movie.index[0]
        movie = movie.squeeze()
        similar_5 = movie.nlargest(6).index
        selected_movies = similar_5[similar_5 != movie_index] 
        return selected_movies
    
