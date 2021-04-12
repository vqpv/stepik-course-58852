n = int(input())

word_list = []

for _ in range(n):
    word = input()
    if word not in word_list:
        word_list.append(word)

print(*word_list, sep='\n')
