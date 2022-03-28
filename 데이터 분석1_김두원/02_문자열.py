str = "korea"
str1 = "fight"
# print(str[3:5]) #[3:5] 모든 파이선 파일에서 가능
# print(type(str))

print(str +" "+str1)

result = "k" not in str1
print(result)

test_str = "i am a boy you are a girl"
print(type(test_str))

print(test_str.count("a"))

print(test_str.find("are"))
print(test_str.index("are"))

str = "korea"
str1 = "fight"

str_result = str + str1
print(str_result)

print(str.join(str1))
# result = str.join(str1)
# print(result)

re_str = " ".join(str)
print(re_str)

aa= " "
print(type(aa))

a, b = 10, 20
print(a,b)

# temp = a
# a = b
# b = temp
# print (a,b)

b, a = a, b
print(a,b)

test_str = "i am a boy you are a girl"
print(test_str.replace("are", "ARE"))

split_text =test_str.split()
print(split_text)
print(type(split_text))

names = "홍길동 홍이동 홍삼동"
kor = "100 90 98"
eng = "88 98 78"
splited_name = names.split()
splited_kor = kor.split()
splited_eng = eng.split()
sum = int(splited_eng[0]) + int(splited_kor[0])
mean = sum/2
print("{0}의 합계{1} 평균{2}".format(splited_name[0],sum,mean))

for x in range(100):
    print(x)
for kor, eng, name in zip(splited_kor, splited_eng), splited_name:
    print(name, kor, eng)

str2 ="a:c:d:f:e"
print(str2.split(":"))
