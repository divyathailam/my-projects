import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def content_based_filtering(movies_path):
    movies = pd.read_csv(movies_path)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

if __name__ == "__main__":
    sim_matrix = content_based_filtering('../data/movies.csv')
    print('Movie similarity matrix (content-based filtering):')
    print(sim_matrix)
