import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

nor_dist = stats.norm(loc=4, scale=0.8)
print(nor_dist)

print(nor_dist.pdf(x=3))
print(nor_dist.pdf(x=4))

x_plot = np.arange(start=1, stop=7.1, step=0.1)
plt.plot(x_plot, stats.norm.pdf(x=x_plot, loc=4, scale=0.8))
print(x_plot)
# plt.show()

np.random.seed(1)
simulated_sample = stats.norm.rvs(loc=4, scale=0.8, size=100000)
print(simulated_sample)

print(simulated_sample <= 3)

cnt_under_3 = np.sum(simulated_sample <= 3)
print("3보다 작은 값의 개수: ", cnt_under_3)
proba_under_3 = cnt_under_3/len(simulated_sample)
print("3이하의 데이터 확률: ", round(proba_under_3, 3)*100, "%")

cnt_under_2 = np.sum(simulated_sample < 3)
cnt_under_5 = np.sum(simulated_sample <= 5)
a = cnt_under_5 - cnt_under_2
proba_under_5 = a/len(simulated_sample)
print("3이상 5이하의 데이터 확률: ", round(proba_under_5, 3)*100, "%")

cnt_3_to_5 = np.sum(np.logical_and(simulated_sample >= 3, simulated_sample <= 5))
proba_3_to_5 = cnt_3_to_5/len(simulated_sample)
print("3이상 5이하의 데이터 확률: ", round(proba_3_to_5, 3)*100, "%")

# 누적 분포 함수 cdf
cumulative_3 = stats.norm.cdf(loc=4, scale=0.8, x=3)
print(cumulative_3)

cumulative_4 = stats.norm.cdf(loc=4, scale=0.8, x=4)
print(cumulative_4)

# ppf (percent point function)

percent_point = stats.norm.ppf(loc=4, scale=0.8, q=0.5)
print(percent_point)

# loc=평균 scale = 표준편차 q = %
# 성적 평균: 85점, 표쥰편차 : 6 일떄 A그룹 8%%이내 A그룹에 들어갈려면 몇점을 받아야하나
score = stats.norm.ppf(loc=85, scale=6, q=0.92)
print(score)
