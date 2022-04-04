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
scores = np.array([80, 79, 76, 50, 66 ,86 ,100 ,40])
cut_score = stats.scoreatpercentile(scores,75)
grade_dic = {}
for score in scores:
    if score >= cut_score:
        grade_dic[score] = "s"
    else:
        grade_dic[score] = "F"
        print(grade_dic)