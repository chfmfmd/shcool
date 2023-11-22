import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_url = 'https://raw.githubusercontent.com/snkn1959/data_source/main/example_cluster.csv'
data = pd.read_csv(file_url)

sns.scatterplot(x='var_1', y = 'var_2', data= data)
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=3, random_state = 100)
kmeans_model.fit(data)
kmeans_model.predict(data)
data['label'] = kmeans_model.predict(data)
sns.scatterplot(x='var_1', y = 'var_2', data= data, hue='label', palette='rainbow')
kmeans_model.inertia_
temp_model = KMeans(n_clusters=500, random_state = 100)
temp_model.fit(data)
temp_model.inertia_
distance = []
for k in range(2,10):
    k_model = KMeans(n_clusters=k)
    k_model.fit(data)
    distance.append(k_model.inertia_)
distance
sns.lineplot(x=range(2,10), y=distance)
plt.show()
file_url = 'https://raw.githubusercontent.com/snkn1959/data_source/main/customer.csv'
customer = pd.read_csv(file_url)
customer.head()
customer['cc_num'].nunique()
customer_dummy = pd.get_dummies(customer, columns =['category'])
customer_dummy.head()
cat_list = customer_dummy.columns[2:]
for i in cat_list:
    customer_dummy[i] = customer_dummy[i] * customer_dummy['amt']
customer_dummy
customer_agg = customer_dummy.groupby('cc_num').sum()
customer_agg.head()
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_df = pd.DataFrame(scaler.fit_transform(customer_agg),
            columns = customer_agg.columns,
            index=customer_agg.index)
scaled_df.head()
distance = []
for k in range(2,10):
    k_model = KMeans(n_clusters=k)
    k_model.fit(scaled_df)
    labels = k_model.predict(scaled_df)
    distance.append(k_model.inertia_)

sns.lineplot(x=range(2,10), y=distance)
from sklearn.metrics import silhouette_score
silhouette = []
for k in range(2, 10):
    k_model = KMeans(n_clusters=k)
    k_model.fit(scaled_df)
    labels = k_model.predict(scaled_df)
    silhouette.append(silhouette_score(scaled_df, labels))
sns.lineplot(x=range(2, 10), y=silhouette)
k_model = KMeans(n_clusters=4)
k_model.fit(scaled_df)
labels = k_model.predict(scaled_df)
scaled_df['label'] = labels
scaled_df_mean = scaled_df.groupby('label').mean()  # ❶
scaled_df_count = scaled_df.groupby('label').count()['category_travel']  # ❷
scaled_df_count = scaled_df_count.rename('count')
scaled_df_all = scaled_df_mean.join(scaled_df_count)
scaled_df_all
