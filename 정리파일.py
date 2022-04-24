import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

a_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 리스트
print(type(a_1))
a = np.array(a_1)  # 넘파이 어레이
a = np.array(a_1)  # 넘파이 어레이
print(type(a))
a_sum = np.sum(a)  # 합
print(a_sum)
a_mean = np.mean(a) # 평균
print(a_mean)
a_var = np.var(a)  #분산
a_var1 = np.var(a, ddof=1)  # 불편분산
print(a_var)
print(a_var1)
a_std = np.std(a, ddof=1)  # 표준편차
print(a_std)
sigma = np.sqrt(a_var)  # 제곱
print(sigma)
# 표준화
stand_fish = a - a_mean
sigma_2 = np.var(a, ddof=1)
sigma = np.sqrt(sigma_2)
stand_sigma = stand_fish/sigma
print(stand_sigma)

a_max = np.max(a) # 최대값
a_min = np.min(a) # 최소값
a_median = np.median(a)  # 중앙값 # 평균값이랑 중앙값이랑 다르다

fish_data4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(stats.scoreatpercentile(fish_data4, 25))
print(stats.scoreatpercentile(fish_data4, 75))
scores1 = np.array([80, 79, 76, 50, 66 ,86 ,100 ,40])
cut_score = stats.scoreatpercentile(scores1,75)
grade_dic = {}
for score in scores1:
    if score >= cut_score:
        grade_dic[score] = "S"
    else:
        grade_dic[score] = "F"
        print(grade_dic)

con_data = pd.read_csv("./data/3-2-3-cov.csv")
print(con_data)

x = con_data["x"]
y = con_data["y"]

# 피어슨 상관 계수
sigma_2_x = np.var(x, ddof=1)
sigma_2_y = np.var(y, ddof=1)
print(sigma_2_x, sigma_2_y)

pi_covar = np.corrcoef(x, y)
print(pi_covar)

fish_multi1 = pd.read_csv("./data/3-2-1-fish_multi.csv")


group = fish_multi1.groupby("species")
print(group.mean())
print(group.max())
print(group.min())
print(group.std(ddof = 1))

print(group.describe())

shoes = pd.read_csv("./data/3-2-2-shoes.csv")
print(type(shoes))
cross = pd.pivot_table(
 data = shoes,
 values = "sales",
 aggfunc = "sum",
 columns = "color")
print(cross)

store_cross = pd.pivot_table(
 data = shoes,
 values = "sales",
 aggfunc = "sum",
 columns = "store")
print(store_cross)

store_cross1 = pd.pivot_table(
 data = shoes,
 values = "sales",
 aggfunc = "sum",
 columns = "store",
 index = "store")
print(store_cross1)

num1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num2 = [2, 3, 4, 3, 5, 4, 6, 7, 4, 8]

x = np.array(num1)
y = np.array(num2)

plt.plot(x, y, color="r")
plt.xlabel("x")
plt.ylabel("y")
# plt.savefig("first") # 저장
# plt.legend
plt.show()

fish_multi2 = pd.read_csv("./data/3-3-2-fish_multi_2.csv")

fish_a = fish_multi2[fish_multi2.species == "A"]  # = fish_multi[fish_multi["species"] == "A"]
fish_b = fish_multi2.query("species == 'B'")

sns.boxplot(data=fish_multi2, x="species", y="length", color="blue") #박스 플롯
plt.show()

fish_multi = pd.read_csv("./data/3-3-2-fish_multi_2.csv")
print(fish_multi)

fish_multi_group = fish_multi.groupby("species") #시본 그래프
print(fish_multi_group)
print(fish_multi_group.describe())

print(fish_multi_group.count())
want_cols = ["species", "length"]
print(fish_multi[want_cols])

print(fish_multi[1:3]["species"])
print(fish_multi.loc[1:3, "species"])

print(fish_multi[fish_multi["species"] == "A"])
# print(fish_multi["species"] == "A")
print(fish_multi[fish_multi.species == "A"][0:3]["length"])
print(fish_multi[fish_multi.species == "A"].loc[0:2, "length"])

print(fish_multi.query("species == 'A'")["length"])

fish_multi = pd.read_csv("./data/3-3-2-fish_multi_2.csv")
print(fish_multi)

fish_a = fish_multi[fish_multi.species == "A"]  # = fish_multi[fish_multi["species"] == "A"]
fish_b = fish_multi.query("species == 'B'")

sns.violinplot(data=fish_multi, x="species", y="length", color="blue") # 바이올린 플롯
plt.show()

fish_multi = pd.read_csv("./data/3-3-2-fish_multi_2.csv")
print(fish_multi)

fish_a = fish_multi[fish_multi.species == "A"]  # = fish_multi[fish_multi["species"] == "A"]
fish_b = fish_multi.query("species == 'B'")
sns.barplot(data=fish_multi, x="species", y="length", palette="husl") #막대그래프
plt.show()

cov_data = pd.read_csv("./data/3-2-3-cov.csv")
print(cov_data)

x = cov_data["x"]
y = cov_data["y"]
print(cov_data.columns)
print(cov_data.index)

scipy_cov = np.cov(x, y, ddof=1)
print(scipy_cov)
# 피어슨 상관 계수
corre = np.corrcoef(x, y, ddof=1)
print(corre)

sns.jointplot(x="x", y="y", data=cov_data, color="black") #산포도
plt.show()

iris = sns.load_dataset("iris")
# print(iris)
# print(type(iris))
# print(iris.columns)
sns.pairplot(iris, hue="species", palette="husl") #페어플롯
plt.show()

data = np.array([1, 2, 3, 4, 5, 6])
print(data)

one = np.random.choice(data, size=3, replace=True)
print(one)


for i in range(len(data)): #데이터를 랜덤으로 뽑을때
    one = np.random.choice(data, size=1, replace=False)
    print(one)


fish_5 = np.array([2, 3, 4, 5, 6])
# print(fish_5.shape)
# print(type(fish_5))
# print(fish_5)
#
# fish = [2, 3, 4, 5, 6]
# print(type(fish))
# print(fish)
#
# np.random.seed(1)  # 랜덤값 고정
# fish_5 = np.array([2, 3, 4, 5, 6])
# choice_one = np.random.choice(fish_5, size=3, replace=True)
# print(choice_one)
#
fish_temp = pd.read_csv("./data/3-4-1-fish_length_100000.csv")
print(type(fish_temp))
print(len(fish_temp))
print(fish_temp.head(5))
print(fish_temp.tail(5))
print(fish_temp.columns)
print(fish_temp.index)
print(fish_temp.values)

fish_a = fish_temp.values
print(type(fish_a))

# 모집단의 평균
print("100,000 마리의 모집단 평균: ", np.mean(fish_a))
fish_temp1 = pd.read_csv("./data/3-4-1-fish_length_100000.csv")["length"]
fish_sample = np.random.choice(fish_temp1, size=10000, replace=False)
print("모집단의 평균: ", np.mean(fish_sample))
print("샘플의 분산 : ", np.var(fish_sample, ddof=0))
print("모집단의 표준 편차 : ", np.std(fish_sample, ddof=0))
print("샘플의 표준 편차 : ", np.std(fish_sample, ddof=1))

#########################################
# data = pd.read_csv("./data/5-1-1-beer.csv")
# # print(data.head(5))
# # print(data.columns)
# # print(data["temperature"].head(5))
# # print(type(data))
# beer_temp = data["temperature"]
#
# data1 = pd.read_csv("./data/5-1-1-beer.csv")["temperature"]
# print(len(data1))
# print(data1.head(5))
# print("모집단의 평균: ", np.mean(data1))
# print("모집단의 표준 분산 : ", np.var(data1))
# print("모집단의 표준 편차 : ", np.std(data1, ddof=1))

# print(beer_temp.head(5))
# print(type(beer_temp))
# print(beer_temp.unique())
#
# beer_temp1 = data[["beer", "temperature"]]
# print(beer_temp1.unique())
#########################################

population = stats.norm(loc=4, scale=0.8)
x = np.linspace(0, 8, 100)
print(x)
# probability density function
print(population.pdf(4*(0.8*1.96)))
y = population.pdf(x)
plt.plot(x, y)
plt.show()

sample_mean_array = np.zeros(10000)
print(sample_mean_array)
population = stats.norm(loc=4, scale=0.8)
np.random.seed(1)
for i in range(10000):
    sample = population.rvs(size=10)
    print(sample)
    sample_mean_array[i] = np.mean(sample)
print(sample_mean_array)
print(np.mean(sample_mean_array))
