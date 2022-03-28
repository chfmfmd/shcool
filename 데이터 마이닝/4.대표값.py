import numpy as np
import scipy as sp

fish_data = np.array([2,3,3,4,4,4,4,6,7,16])
print(np.mean(fish_data))
print("최대값 : {}, 최소값 : {} ".format(np.max(fish_data),np.min(fish_data)))
print("중앙값 : ", np.median(fish_data)) # 평균값이랑 중앙값이랑 다르다

from scipy import stats
fish_data = np.array([1,2,3,4,5,6,7,8,9])
print(stats.scoreatpercentile(fish_data, 25))
print(stats.scoreatpercentile(fish_data, 75))
score = np.array([80, 79, 76, 50, 66 ,86 ,100 ,40]) # 상위 25% S 뜨게 만들기
cut_score = stats.scoreatpercentile(score,75)
grade = []
#for score in scores:
    #if scores >= cut_score:
    #grade.append("S")
#else:
    #grade.append("F")
    #print(grade)