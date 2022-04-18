import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

population = stats.norm(loc=4, scale=0.8)
x = np.linspace(0, 8, 100)
# # print(x)
# probability density function
# print(population.pdf(4*(0.8*1.96)))
y = population.pdf(x)
plt.plot(x, y)
# plt.show()

sample_mean_array = np.zeros(10000)
# print(sample_mean_array)
population = stats.norm(loc=4, scale=0.8)
np.random.seed(1)
for i in range(0, 10000):
    sample = population.rvs(size=10)
    # print(sample)
    sample_mean_array[i] = np.mean(sample)
print(sample_mean_array)
print(np.mean(sample_mean_array))