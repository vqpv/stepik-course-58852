a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (a == c or a == c - 1 or a == c + 1) and (b == d or b == d - 1 or b == d + 1):
    print("YES")
else:
    print("NO")
