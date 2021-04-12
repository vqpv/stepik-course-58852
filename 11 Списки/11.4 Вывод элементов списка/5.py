n = int(input())

string_list = []

for _ in range(n):
    string_list.append(input())

search_word = input()

for string in string_list:
    if search_word.lower() in string.lower():
        print(string)
