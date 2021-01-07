import math

n = int(input())

summa = 1

for i in range(2, n + 1):
    summa += 1 / i

print(summa - math.log(n))
