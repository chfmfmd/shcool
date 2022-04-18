import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# seri_1 = pd.Series(["a", "b", "c", "d"])
# print(type(seri_1))
# print(seri_1)
# print(seri_1[0])
# seri_1[1] = "xxx"
# print(seri_1)
# print(seri_1.index)
# print(seri_1.values)
# print(type(seri_1.values))
# print(seri_1[1:3])
#
# seri_2 = pd.Series([221,32,4,5,43,564,6,35])
# print(np.sum(seri_2.values))
#
# kor_score_seri = pd.Series([88, 78, 68, 58], index=["홍", "박", "김", "최"], dtype="float")
# print(kor_score_seri)
# eng_score_seri = pd.Series([188, 178, 168, 158], dtype="float")
# name = ["홍", "박", "김", "최"]
# eng_score_seri.index = name
# print(eng_score_seri)
#
# dict1 = {"홍" :98 , "박":99 , "최":100 }
# # print(dict1)
# # print(dict1.keys())
# # print(dict1.values())
# # print(dict1.items())
# student_seri = pd.Series(dict1)
# print(student_seri)
#
# dic2 = {"국어" : [10, 11, 12], "영어" : [21,22,23], "수학" : [31, 32, 33]}
# student_seri2 = pd.Series(dic2)
# print(student_seri2)
#
# sub = ["국어", "영어", "수학"]
# kor = [10, 11, 12]
# eng = [21, 22, 23]
# math = [31, 32, 33]
# dic3 = {sub[0] : kor, sub[1] : eng, sub[2] : math}
# student_seri3 = pd.Series(dic3)
# print(student_seri3)
#
#
#
# student_seri3.name = "학생성적"
# student_seri3.index.name = "과목이름"
# # print(student_seri3)
#
# data = pd.read_csv("./data/3-2-2-shoes.csv")
# print(type(data))
# print(data)
# print(data.columns)
# print(data.index[1])
# print(data[["store", "sales"]])
# print(np.sum(data["sales"]))
#
# # 판매개수가 10개 미만인 가계이름 출력
# total_sale = data["sales"].sum()
# print("총 판매 개수 :" , np.sum(data["sales"]))
# shop_name = data[data["sales"] < 10]
# print(shop_name["store"].values)

data = pd.read_csv("./data/3-2-2-shoes.csv")
print(data)
print(np.sum(data[data["store"] == "tokyo"]["sales"]))
blue = np.sum(data[data["color"] == "blue"]["sales"])
red = np.sum(data[data["color"] == "red"]["sales"])
print("파란색 : {}  빨간색 : {} ".format(blue,red))