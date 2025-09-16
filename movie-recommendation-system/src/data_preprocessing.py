import pandas as pd

def preprocess_ratings(ratings_path):
    ratings = pd.read_csv(ratings_path)
    # Example: Remove duplicates, handle missing values
    ratings = ratings.drop_duplicates()
    ratings = ratings.dropna()
    return ratings

def preprocess_movies(movies_path):
    movies = pd.read_csv(movies_path)
    # Example: Remove duplicates
    movies = movies.drop_duplicates()
    return movies

if __name__ == "__main__":
    ratings = preprocess_ratings('../data/ratings.csv')
    movies = preprocess_movies('../data/movies.csv')
    print('Preprocessing complete.')
