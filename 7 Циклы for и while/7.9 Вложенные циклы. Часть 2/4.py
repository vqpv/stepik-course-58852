n = int(input())

for i in range(1, n + 1):
    count_divisors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count_divisors += 1
    print(i, "+" * count_divisors, sep="")
