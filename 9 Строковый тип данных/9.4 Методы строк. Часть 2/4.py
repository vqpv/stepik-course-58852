string = input()

count = 0

for char in string:
    if char.isdigit():
        count += 1

print(count)
