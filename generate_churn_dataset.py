import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of customers
n_customers = 8000

# Generate synthetic features
data = pd.DataFrame({
    'CustomerID': np.arange(1, n_customers + 1),
    'Age': np.random.randint(18, 70, n_customers),
    'Gender': np.random.choice(['Male', 'Female'], n_customers),
    'Tenure': np.random.randint(1, 10, n_customers),
    'Balance': np.random.uniform(0, 100000, n_customers),
    'NumOfProducts': np.random.randint(1, 5, n_customers),
    'HasCrCard': np.random.choice([0, 1], n_customers),
    'IsActiveMember': np.random.choice([0, 1], n_customers),
    'EstimatedSalary': np.random.uniform(10000, 150000, n_customers)
})

# Simulate churn based on some features
churn_prob = (
    0.2 * (data['Tenure'] < 3).astype(int) +
    0.3 * (data['IsActiveMember'] == 0).astype(int) +
    0.2 * (data['Balance'] < 20000).astype(int) +
    0.1 * (data['NumOfProducts'] == 1).astype(int) +
    0.2 * np.random.rand(n_customers)
)
data['Churn'] = (churn_prob > 0.5).astype(int)

data.to_csv('customer_churn_data.csv', index=False)
print('Synthetic dataset created: customer_churn_data.csv')
