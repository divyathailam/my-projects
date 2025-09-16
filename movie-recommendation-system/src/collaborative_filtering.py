import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def collaborative_filtering(ratings_path):
    ratings = pd.read_csv(ratings_path)
    user_movie_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    similarity = cosine_similarity(user_movie_matrix)
    similarity_df = pd.DataFrame(similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)
    return similarity_df

if __name__ == "__main__":
    sim_df = collaborative_filtering('../data/ratings.csv')
    print('User similarity matrix (collaborative filtering):')
    print(sim_df)
