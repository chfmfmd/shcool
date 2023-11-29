import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
import time

# 고객 데이터를 불러와서 처음 5개 행을 확인합니다.
file_url = 'https://raw.githubusercontent.com/snkn1959/data_source/main/customer_pca.csv'
customer = pd.read_csv(file_url)
customer.head()

# 입력 데이터와 레이블을 분리합니다.
customer_X = customer.drop('label', axis=1)
customer_y = customer['label']

# 주성분 분석 (PCA)을 수행합니다.
pca = PCA(n_components=2)
pca.fit(customer_X)
customer_pca = pca.transform(customer_X)
customer_pca

# PCA 결과를 데이터프레임으로 변환하고 레이블과 결합합니다.
customer_pca = pd.DataFrame(customer_pca, columns=['PC1', 'PC2'])
customer_pca = customer_pca.join(customer_y)
customer_pca.head()

# Scatter plot을 이용하여 PCA 결과를 시각화합니다.
sns.scatterplot(x='PC1', y='PC2', data=customer_pca, hue='label', palette='rainbow')
plt.show()

# PCA 주성분을 확인합니다.
pca.components_
df_comp = pd.DataFrame(pca.components_, columns=customer_X.columns)
sns.heatmap(df_comp, cmap='coolwarm')
plt.show()

# 익명의 데이터를 불러옵니다.
file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/anonymous.csv'
anonymous = pd.read_csv(file_url)
anonymous.head()
anonymous['class'].mean()
anonymous.isna().sum().sum()

# 익명의 데이터를 훈련 세트와 테스트 세트로 분할합니다.
X_train, X_test, y_train, y_test = train_test_split(anonymous.drop('class', axis=1), anonymous['class'], test_size=0.2,
                                                    random_state=100)

# 표준화를 위해 스케일러를 사용합니다.
scaler = StandardScaler()
scaler.fit(X_train)

# 스케일링된 데이터를 얻습니다.
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 첫 번째 랜덤 포레스트 모델을 생성하고 훈련합니다.
model_1 = RandomForestClassifier(random_state=100)

start_time = time.time()
model_1.fit(X_train_scaled, y_train)
print(time.time() - start_time)

# 첫 번째 모델의 성능을 평가합니다.
pred_1 = model_1.predict(X_test_scaled)
accuracy_score(y_test, pred_1)

proba_1 = model_1.predict_proba(X_test_scaled)
roc_auc_score(y_test, proba_1[:, 1])

# 주성분의 설명된 분산 비율을 확인하고 시각화합니다.
pca = PCA(n_components=2)
pca.fit(X_train_scaled)
pca.explained_variance_ratio_
var_ratio = []

for i in range(100, 550, 50):
    pca = PCA(n_components=i)
    pca.fit_transform(X_train_scaled)
    ratio = pca.explained_variance_ratio_.sum()
    var_ratio.append(ratio)

sns.lineplot(x=range(100, 550, 50), y=var_ratio)
plt.show()

# 주성분의 수를 고려하여 PCA를 적용한 후 모델을 생성하고 훈련합니다.
pca = PCA(n_components=400, random_state=100)
pca.fit(X_train_scaled)
X_train_scaled_pca = pca.transform(X_train_scaled)
X_test_scaled_pca = pca.transform(X_test_scaled)

model_2 = RandomForestClassifier(random_state=100)
start_time = time.time()
model_2.fit(X_train_scaled_pca, y_train)
print(time.time() - start_time)

# 두 번째 모델의 성능을 평가합니다.
pred_2 = model_2.predict(X_test_scaled_pca)
accuracy_score(y_test, pred_2)

proba_2 = model_2.predict_proba(X_test_scaled_pca)
roc_auc_score(y_test, proba_2[:, 1])
