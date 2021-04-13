n = int(input())

string_list = []
words_list = []

for _ in range(n):
    string_list.append(input())

word_count = int(input())

for _ in range(word_count):
    words_list.append(input().lower())

for string in string_list:
    flag = 0
    for word in words_list:
        if word in string.lower():
            flag += 1
    if len(words_list) == flag:
        print(string)
