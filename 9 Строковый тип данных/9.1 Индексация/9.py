string = input()

count = 0

for index in range(len(string) - 2):
    if string[index] == string[index + 1]:
        count += 1

print(count)