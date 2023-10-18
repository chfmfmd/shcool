import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

# 데이터 불러오기
df = pd.read_csv('https://media.githubusercontent.com/media/musthave-ML10/data_source/main/salary.csv', skipinitialspace=True)

# 'class' 열의 값을 0과 1로 매핑
df['class'] = df['class'].map({'<=50K': 0, '>50K': 1})

# 데이터 정보 출력
df.info()

# 데이터 통계 정보 출력 (object 변수 포함)
df.describe(include='all').T

# 각 열의 데이터 타입 확인
for i in df.columns:
    print(i, df[i].dtype)

# object 타입 열의 이름을 리스트에 추가
obj = []
for i in df.columns:
    if df[i].dtype == 'object':
        obj.append(i)

# object 타입 열 중 유니크 값이 10 이상인 열의 이름 출력
for i in obj:
    if df[i].nunique() >= 10:
        print(i, df[i].nunique())

# 'education' 열 삭제
df.drop('education', axis=1, inplace=True)

# 'occupation' 열의 고유값 확인
df['occupation'].value_counts()

# 'native-country' 열의 고유값 확인
df['native-country'].value_counts()

# 'native-country' 그룹별 'class' 열의 평균값 계산 후 정렬
group = df.groupby('native-country')['class'].mean()

# 'group' 변수에 저장
group

# 'group' 변수를 데이터프레임으로 변환
group = group.reset_index()

# 'native-country' 열 삭제 및 이름 변경
df = df.merge(group, on='native-country', how='left')
df.drop('native-country', axis=1, inplace=True)
df = df.rename(columns={'class_x': 'class', 'class_y': 'native-country'})

# 결측치 비율 확인
df.isna().mean()

# 'native-country' 열의 결측치를 -99로 채움
df['native-country'] = df['native-country'].fillna(-99)

# 'workclass' 열의 고유값 확인
df['workclass'].value_counts()

# 'workclass' 열의 결측치를 'Private'로 채움
df['workclass'] = df['workclass'].fillna('Private')

# 'occupation' 열의 고유값 확인
df['occupation'].value_counts()

# 'occupation' 열의 결측치를 'Unknown'으로 채움
df['occupation'] = df['occupation'].fillna('Unknown')

# 모든 열을 더미 변수로 변환
df = pd.get_dummies(df, drop_first=True)

# 학습 및 테스트 데이터 분할
xtr, xt, ytr, yt = train_test_split(df.drop('class', axis=1), df['class'], test_size=0.4, random_state=100)

# 의사결정나무 분류 모델 생성
dt = DecisionTreeClassifier()
dt.fit(xtr, ytr)

# 테스트 데이터에 대한 예측 수행
pred = dt.predict(xt)

# 정확도 출력
accuracy_score(yt, pred)

# 최대 깊이를 설정한 의사결정나무 모델 생성
dt = DecisionTreeClassifier(max_depth=7)
dt.fit(xtr, ytr)
train_pred = dt.predict(xtr)
test_pred = dt.predict(xt)

# 학습 데이터와 테스트 데이터에 대한 정확도 출력
print(accuracy_score(ytr, train_pred))
print(accuracy_score(yt, test_pred))

# 의사결정나무 시각화
plt.figure(figsize=(30, 15))
plot_tree(dt, max_depth=3, fontsize=15, feature_names=xtr.columns)
plt.show()
