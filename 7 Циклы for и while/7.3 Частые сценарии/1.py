a, b = int(input()), int(input())

s = 0

for i in range(a, b + 1):
    if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
        s += 1

print(s)
