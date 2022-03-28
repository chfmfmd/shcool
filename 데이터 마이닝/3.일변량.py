import numpy as np
import scipy as sp

fish_data = np.array([2,3,3,4,4,4,4,5,5,6])
print(fish_data)
print("{} 마리의 무게 합 {:3.2f} :".format(len(fish_data),np.sum(fish_data)))

N = len(fish_data)
sum_value =  np.sum(fish_data)
mu = sum_value/len(fish_data)
print("평균값 {:2.3f}" .format(mu))
print("평균값 {:2.3f}" .format(np.mean(fish_data)))

x = np.array([1,2,3,4])
x1 = x +10
print(x1)

# 편차
user_var = np.sum((fish_data-mu)**2) /(N-1)
print(user_var)
print(np.var(fish_data, ddof=1))
print(np.std(fish_data))

sigma_2 = np.var(fish_data, ddof=1)
sigma = np.sqrt(sigma_2)
print(sigma)

#표준편차
stand_sigma = np.std(fish_data, ddof=1)
print(stand_sigma)

#표준화
stand_fish = fish_data -mu
print(stand_fish)
print(np.mean(stand_fish))

print(fish_data/sigma)
print(np.std(fish_data/sigma ,ddof=1))
stand_sigma =stand_fish/sigma
print(stand_sigma)