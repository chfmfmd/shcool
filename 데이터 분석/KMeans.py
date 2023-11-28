import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

file_url = 'https://raw.githubusercontent.com/snkn1959/data_source/main/example_cluster.csv'
data = pd.read_csv(file_url)

# 산점도 그리기
sns.scatterplot(x='var_1', y='var_2', data=data)
plt.show()

# K-Means 모델 생성 및 학습
kmeans_model = KMeans(n_clusters=3, random_state=100)
kmeans_model.fit(data)
kmeans_model.predict(data)
data['label'] = kmeans_model.predict(data)

# 산점도에 클러스터 레이블 표시
sns.scatterplot(x='var_1', y='var_2', data=data, hue='label', palette='rainbow')
plt.show()
kmeans_model.inertia_

# 임시 K-Means 모델 생성 및 학습
temp_model = KMeans(n_clusters=500, random_state=100)
temp_model.fit(data)
temp_model.inertia_

# 클러스터 개수에 따른 K-Means 모델의 이너셔 그래프 그리기
distance = []
for k in range(2, 10):
    k_model = KMeans(n_clusters=k)
    k_model.fit(data)
    distance.append(k_model.inertia_)

sns.lineplot(x=range(2, 10), y=distance)
plt.show()

file_url = 'https://raw.githubusercontent.com/snkn1959/data_source/main/customer.csv'
customer = pd.read_csv(file_url)
customer.head()
customer['cc_num'].nunique()

# 범주형 변수 더미화
customer_dummy = pd.get_dummies(customer, columns=['category'])
customer_dummy.head()

# 범주형 변수에 'amt' 곱하기
cat_list = customer_dummy.columns[2:]
for i in cat_list:
    customer_dummy[i] = customer_dummy[i] * customer_dummy['amt']
customer_dummy

# 고객별로 그룹화하고 합계 계산
customer_agg = customer_dummy.groupby('cc_num').sum()
customer_agg.head()

# 데이터 표준화
scaler = StandardScaler()
scaled_df = pd.DataFrame(scaler.fit_transform(customer_agg),
                        columns=customer_agg.columns,
                        index=customer_agg.index)
scaled_df.head()

# 클러스터 개수에 따른 K-Means 모델의 이너셔 그래프 그리기
distance = []
for k in range(2, 10):
    k_model = KMeans(n_clusters=k)
    k_model.fit(scaled_df)
    labels = k_model.predict(scaled_df)
    distance.append(k_model.inertia_)

sns.lineplot(x=range(2, 10), y=distance)
plt.show()

# 실루엣 스코어 계산 및 그래프 그리기
silhouette = []
for k in range(2, 10):
    k_model = KMeans(n_clusters=k)
    k_model.fit(scaled_df)
    labels = k_model.predict(scaled_df)
    silhouette.append(silhouette_score(scaled_df, labels))

sns.lineplot(x=range(2, 10), y=silhouette)
plt.show()

# 최종 K-Means 모델 학습 및 클러스터 레이블 할당
k_model = KMeans(n_clusters=4)
k_model.fit(scaled_df)
labels = k_model.predict(scaled_df)
scaled_df['label'] = labels

# 클러스터별로 평균 및 개수 계산
scaled_df_mean = scaled_df.groupby('label').mean()
scaled_df_count = scaled_df.groupby('label').count()['category_travel']
scaled_df_count = scaled_df_count.rename('count')
scaled_df_all = scaled_df_mean.join(scaled_df_count)
scaled_df_all
