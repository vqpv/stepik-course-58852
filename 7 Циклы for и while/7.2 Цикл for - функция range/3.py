m, n = int(input()), int(input())

for i in range(m + 1, n, -1):
    if i % 2 == 1:
        print(i)
