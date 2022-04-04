from typing import List

import numpy as np

dic_1 = {"kor": 94, "eng": 80, "math": 90}
print(type(dic_1))
print(dic_1)
print(dic_1["kor"])
dic_1["kor"] = 100
print(dic_1)
print(dic_1["kor"])
print(dic_1.keys())
print(dic_1.values())
print(dic_1.items())

sum = 0
for key, value in dic_1.items():
    print("{}는 {}점 입니다".format(key, value))
    sum = sum + value
print("평균은 {}점입니다".format(sum / len(dic_1)))

kor_scores = [93, 80, 98, 78]
eng_scores = [92, 82, 92, 74]
math_scores = [90, 80, 70, 80]
dic_2 = {"Kor": kor_scores, "Eng": eng_scores, "Math": math_scores}
print(dic_2)

sum_kor = 0
sum_eng = 0
sum_math = 0
for key, value in enumerate(dic_2.items()):
    if key == "Kor":
        sum_kor = np.sum(value)
    if key == "Eng":
        sum_eng = np.sum(value)
    if key == "Math":
        sum_math = np.sum(value)
print(sum_kor)
print(sum_eng)
print(sum_math)

for key, value in dic_2.items():
    print("{}의 평균은 {}점 입니다".format(key, np.mean(value)))

dic_2["history"] = [89, 99, 79, 69]
print(dic_2)

dic_2["history"] = [19, 19, 19, 19]
print(dic_2)

word_k = ["아버지", "어머니", "동생"]
word_e = ["father", "mother", "brother"]

dic_word = {}
for i in range(len(word_k)):
    dic_word[word_k[i]] = word_e[i]
print(dic_word)

ex_dic1 = {}
for key, value in zip(word_k, word_e):
    ex_dic1[key] = value
print(ex_dic1)
x = []
y = []
z = []
scores = [80, 79, 97, 93, 79, 99, 86, 99]
class_dic = {90: [], 80: [], 70: []}
for i in range(len(scores)):
    if scores[i] >= 90:
        x.append(scores[i])
    elif scores[i] >= 80:
        y.append(scores[i])
    else: z.append(scores[i])
class_dic[90] = x
class_dic[80] = y
class_dic[70] = z
for key, value in class_dic.items():
    print("{}점 이상을 {}명 입니다".format(key, len(value)))


strings = ["java", "python", "a", "bb", "aacd", "father", "mm", "oh", "ccc", "ddd", "c"] #글자수 만큼 딕셔너리 키 만들고 그 글자수 키값에 단어 넣기
dic = {}
print(s)
print(len(strings[0:]))

