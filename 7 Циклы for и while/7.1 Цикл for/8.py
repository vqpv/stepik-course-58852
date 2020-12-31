m, p, n = int(input()), int(input()) / 100, int(input())

for i in range(n):
    print(i + 1, m)
    m = m * (p + 1)
