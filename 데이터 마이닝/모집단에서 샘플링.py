import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt

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