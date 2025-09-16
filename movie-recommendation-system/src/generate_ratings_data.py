import pandas as pd
import numpy as np

# Sample ratings data
data = {
    'userId': np.repeat([1, 2, 3, 4, 5], 5),
    'movieId': list(range(1, 6)) * 5,
    'rating': np.random.randint(1, 6, 25)
}
df = pd.DataFrame(data)
df.to_csv('data/ratings.csv', index=False)
print('Sample ratings.csv created.')
