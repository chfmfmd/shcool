import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

fish = pd.read_csv("./data/3-7-1-fish_length.csv")
print(fish)
mu = fish.mean()
print("물고기 무게:", mu)
print("물고기 무게", np.mean(fish))

df = len(fish) - 1
df1 = fish.size - 1
print("자유도:", df, df1)

#  표준편차
sigma = np.std(fish, ddof=1)
print("분산값:", sigma)

#  표준오차
se = sigma/np.sqrt(df)

# 신뢰구간
interval =stats.t.interval(alpha=0.95, df=df, loc=mu, scale=0.8)
print(interval)