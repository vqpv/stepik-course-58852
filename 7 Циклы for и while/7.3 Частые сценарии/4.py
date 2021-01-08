n = int(input())

summa = 0

for i in range(n + 1):
    if (i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10 == 8:
        summa += i

print(summa)
