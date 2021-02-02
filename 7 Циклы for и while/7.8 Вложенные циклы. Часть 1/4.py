n = int(input())

for i in range(n):
    r = (n // 2 + 1) - abs(n // 2 - i)
    for _ in range(r):
        print('*', end='')
    print()
