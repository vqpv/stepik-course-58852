n = int(input())

summa = 0

while n != 0:
    summa += n % 10
    n = n // 10
    while summa > 9:
        summa -= 9

print(summa)
