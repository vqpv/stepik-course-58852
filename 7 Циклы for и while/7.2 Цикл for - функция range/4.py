m, n = int(input()), int(input())

for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif (i % 3 == 0) and (i % 5 == 0):
        print(i)
