import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(1)
t_value_array = np.zeros(10000)
norm_dist = stats.norm(loc=4, scale=0.8)

for i in range(0,10000):
    sample = norm_dist.rvs(size=10)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    sample_se = sample_std / np.sqrt(len(sample))
    t_value_array[i] = (sample_mean - 4) / sample_se

# print(t_value_array)

x = np.arange(start=-8, stop= 8.1, step=0.1)
sns.distplot(t_value_array, color="blue")
# plt.plot(x, stats.norm.pdf(x=x), color="black", linestyle="dotted")
# plt.show()
# plt.plot(x, stats.t.pdf(x=x, df=9), color="red")
plt.show()
