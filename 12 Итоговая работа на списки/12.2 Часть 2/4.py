number = input().split('-')

count = 0
length = [len(_) for _ in number]

for i, _ in enumerate(number):
    if number[i].isdigit():
        if (length == [3, 3, 4]) or (number[0] == '7' and length == [1, 3, 3, 4]):
            count += 1

if count == len(number):
    print('YES')
else:
    print('NO')
