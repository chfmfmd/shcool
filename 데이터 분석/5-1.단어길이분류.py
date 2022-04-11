strings = ["aa", "cccc", "aa", "b", "bb", "ccc", "x", "sdfsfss", "c"]
max_word_length = 0
for count in range(len(strings)):
    if max_word_length <= len(strings[count]):
        max_word_length = len(strings[count])
print(max_word_length)

word_count = {}
key_list = list(range(1, max_word_length+1))
print(key_list)
temp_list = list()
for x in range(max_word_length):
    for word in strings:
        if len(word) == key_list[x]:
            temp_list.append(word)
    word_count[key_list[x]] = temp_list
    temp_list = []
print(word_count)

x = []
for i in strings:
     mean = len(i)
     x.append(mean)
dic = {}
for key, value in zip(x, strings):
    if key in dic:
        dic[key].append(value)
    else:
        temp = list()
        temp.append(value)
        dic[key] = temp
print(dic)
