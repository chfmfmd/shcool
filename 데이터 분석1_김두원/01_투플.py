tup1 = 2
a = 3
print(a)
print(type(a))

tup1= (2,3,4)
print(tup1)
print(type(tup1))

len = len(tup1)
print(tup1[0:len])

# tup1[1] = 10 tup는 한번넣으면 값이 안바뀜

tup2 =[1, 12, (1,2,3,(10,20,30)), 20] # 다른데이터라도 들어감 대신 한번밖에 안들어감
print(tup2[0])
print(tup2[2][3][:2])

tup3 = [2,3,4]
print(type(tup3))

tup1= (2, 3, 4)
tup2= (10, 20, 30)
print(tup1 + tup2)

