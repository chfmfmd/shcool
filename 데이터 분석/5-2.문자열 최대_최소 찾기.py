strings = ["father", "boy", "good", "xxx", "sdfsdfs", "ccccc", "girl", "cow", "Register", "csc", "sdfsdfsdf", "dcd"]

print(max(strings, key=len))
print(min(strings, key=len))

max_word_length = 0
max_word = []
min_word_length = 100
min_word = []

for word in strings:
    if len(word) >= max_word_length:
        max_word_length = len(word)
        max_word.append(word)
    if len(word) <= min_word_length:
        min_word_length = len(word)
        min_word.append(word)
min_word.remove("father")
print(max_word)
print(min_word)

print("최대 길이 단어 : {} 최소 길이 단어 : {}".format(max_word, min_word))

min_word_length =3
min_word_list = []
for word in strings:
    if len(word) == min_word_length:
        min_word_list.append(strings.index(word))

for x in min_word_list:
    print(strings[x])

min_word = []
for word in strings:
    if min_word_length == len(word):
        min_word.append(word)
print(min_word)

for word in min_word:
    print(word)

c_list = []
for word in strings:
    if word[0] == "c":
        c_list.append(word)
print(c_list)

# 단어 시작이 같은 문자인 단어 딕셔너리 분류
# 예시 A : [Apple. animal] B:[Banna,bug]
word = ["shop", "very", "often", "prize", "fix", "judge", "together", "sentence", "knowledge", "sure", "only",
        "dangerous", "short", "contest", "homeroom", "apple", "wise", "worry", "about", "finally", "pizza"]
x = []
for i in word:
     y = i[0]
     x.append(y)
dic = {}
for key, value in zip(x, word):
    if key in dic:
        dic[key].append(value)
    else:
        temp = list()
        temp.append(value)
        dic[key] = temp
print(dic)
