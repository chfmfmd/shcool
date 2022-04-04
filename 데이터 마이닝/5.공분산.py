import pandas as pd
import numpy as np
import scipy as sp

# sam = [3, 2, 5, 9, 2, 4, 9]
# mean = np.mean(sam)  평균
# var = np.var(sam, ddof=1)  분산
# std = np.std(sam, ddof=1)  표준편차
# print(mean, var, std)

con_data = pd.read_csv("./data/3-2-3-cov.csv")
print(con_data)

x = con_data["x"]
y = con_data["y"]

n = len(con_data)
print(n)

mu_x = np.mean(x)
mu_y = np.mean(y)
print("x 변수의 평균값은 : ", mu_x)
print("y 변수의 평균값은 : ", mu_y)

con_sample = np.sum((x - mu_x) * (y - mu_y)) / n
print("x - y의 공분산 : ", con_sample)

con_sample1 = np.sum((x - mu_x) * (y - mu_y)) / (n - 1)
print("x - y의 불편 공분산 : ", con_sample1)

con_variance = np.cov(x, y, ddof=0)
print(con_variance)
# con_variance = sp.cov(x, y, ddof=0)

con_variance1 = np.cov(x, y, ddof=1)
print(con_variance1)

# 피어슨 상관 계수
sigma_2_x = np.var(x, ddof=1)
sigma_2_y = np.var(y, ddof=1)
print(sigma_2_x, sigma_2_y)

pi_covar = np.corrcoef(x, y)
print(pi_covar)


