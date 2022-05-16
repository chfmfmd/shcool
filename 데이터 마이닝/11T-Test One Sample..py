import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# T-test = (표본평균 - 비교대상값)/ 표준오차/np.sprt(샘플사이즈)
# T-test = (표본평균 - 비교대상값)/표준오차

junk_food = pd.read_csv("./data/3-8-1-junk-food-weight.csv")
print(junk_food)

# 평균
x_bar = np.mean(junk_food)
# 자유도
df = len(junk_food)-1
# 표준 편차
s = np.std(junk_food, ddof=1)

# 표준 오차
se = s/np.sqrt(len(junk_food))
t_value = (x_bar-50) / se
print("T value", t_value)

alpha = stats.t.cdf(t_value, df=df)
print("알파값", alpha)

print("상한값", (1-alpha)*2)

result = stats.ttest_1samp(junk_food, 50)
print(result)
t_value, p_value = result
print(t_value,p_value)

if p_value < 0.05:
    print("junk_food의 질량은 50g이 아닙니다")
else:
    print("junk_food의 질량은 50g이다")

print(np.mean(junk_food))