string = input().split()

for i, word in enumerate(string):
    string[i] = word[1:] + word[0] + 'ки'

print(*string)
