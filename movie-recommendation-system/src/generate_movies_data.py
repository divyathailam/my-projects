import pandas as pd

# Sample movies data
data = {
    'movieId': [1, 2, 3, 4, 5],
    'title': [
        'Toy Story (1995)',
        'Jumanji (1995)',
        'Grumpier Old Men (1995)',
        'Waiting to Exhale (1995)',
        'Father of the Bride Part II (1995)'
    ],
    'genres': [
        'Adventure|Animation|Children|Comedy|Fantasy',
        'Adventure|Children|Fantasy',
        'Comedy|Romance',
        'Comedy|Drama|Romance',
        'Comedy'
    ]
}
df = pd.DataFrame(data)
df.to_csv('data/movies.csv', index=False)
print('Sample movies.csv created.')
