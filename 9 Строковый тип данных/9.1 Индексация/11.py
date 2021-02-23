num = int(input())

b = ""

while num != 0:
    n = num % 2
    num = num // 2
    b += str(n)

print(b[::-1])
