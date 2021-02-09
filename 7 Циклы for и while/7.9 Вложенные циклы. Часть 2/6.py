n = int(input())

summa = 0

for i in range(1, n + 1):
    comp = 1
    for j in range(1, i + 1):
        comp *= j
    summa += comp

print(summa)
