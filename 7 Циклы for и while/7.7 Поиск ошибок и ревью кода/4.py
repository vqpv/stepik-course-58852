n = int(input())
digits = []

while n != 0:
    digit = n % 10
    if digit % 3 == 0:
        digits.append(digit)
    n = n // 10

if digits:
    print(max(digits))
else:
    print("NO")
