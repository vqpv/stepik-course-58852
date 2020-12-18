num = int(input())

rim_nums = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

if 1 <= num <= 10:
    for i, j in enumerate(rim_nums):
        if num == i + 1:
            print(j)
else:
    print("ошибка")
