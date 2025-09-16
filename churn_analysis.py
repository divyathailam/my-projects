import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('customer_churn_data.csv')

# Encode categorical variables
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Features and target
features = ['Age', 'Gender', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
X = data[features]
y = data['Churn']

# 1. Logistic Regression for Churn Prediction
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)
print('Logistic Regression Classification Report:\n', report)

# 2. PCA for Dimensionality Reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
data['PCA1'] = X_pca[:, 0]
data['PCA2'] = X_pca[:, 1]

# 3. KMeans Clustering to Identify Segments
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_pca)

# Save results for Tableau
result_cols = features + ['Churn', 'PCA1', 'PCA2', 'Cluster']
data[result_cols].to_csv('churn_analysis_results.csv', index=False)

# Visualize clusters (optional)
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=data, palette='Set1')
plt.title('Customer Segments by PCA and KMeans')
plt.savefig('churn_clusters.png')
plt.close()

# Churn rate by cluster
churn_by_cluster = data.groupby('Cluster')['Churn'].mean()
print('Churn rate by cluster:\n', churn_by_cluster)
