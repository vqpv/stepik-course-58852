num = int(input())

a = ""

while num != 0:

    a += str(num % 10)

    num = num // 10

print(a)
