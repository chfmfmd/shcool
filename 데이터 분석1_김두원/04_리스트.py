import numpy as np
from numpy import split

list_1 = [1, 3.1, "가나"]
print(type(list_1))
print(list_1)
print(list_1[1])
list_1.append("추가값")
print(list_1)
list_1.insert(1,"사이값")
print(list_1)
list_1.remove("가나")
print(list_1)

list_2 = list((1,2,3,))
print(type(list_2))

list_1 = [-1, 3.1, -2.0, 0]
for val in list_1:
    if (val) > 0:
        print("양수")
    elif (val) < 0:
        print("음수")
    else:
        print("영")

for i in range(10):
    print(i)

student_avg = []
kor = [99, 80, 89, 98]
math = [80, 89 ,90 ,87]
eng = [90, 98, 80, 79]
for idx in range(4):
    mean = (kor[idx] + math[idx] + eng[idx])/3
    student_avg.append(mean)
print(student_avg)

avg_subject =[]
student_scores= [[99, 80, 89, 98],
                 [80, 89, 90, 87],
                 [90, 98, 80, 79]]
for idx_x in range(3):
    sum = 0
    for idx_y in range(4):
        #print(student_scores[idx_x][idx_y])
        sum = sum + student_scores[idx_x][idx_y]
        avg = sum /4
        avg_subject.append(avg)
print(avg)

word_list =["aaa", "bbbb", "cccccc" ,"dd"]
print(max(word_list, key=len))
count = 0
for word in word_list:
    if len(word) > count:
        count = len(word)
        longest_word = word
print(longest_word)

student_scores= [[90, 93, 90, 90],
                 [80, 86, 80, 91],
                 [70, 76, 88, 70]]
# 각렬의 최고 점수 구하기
for x in range(3):
 max_score = -100
 for y in range(4):
    if max_score < student_scores[x][y]:
       max_score = student_scores[x][y]
       loc_x, loc_y = x , y
       print("{}번 쨰 학생의 점수 {}".format(loc_y+1, student_scores[loc_x]))


list1 = ["a", "b", "c"]
list2 = ["A", "B" ,"C"]
#for i in range(3):
   # print(list1[i])
   # print(list2[i])
#for val1, val2 in zip(list2, list1):
  #  print(val1, val2)

word_list = ["xaaa", "xabc", "cccccc", "dd"]
#for val in word_list:
 #   print(val)
