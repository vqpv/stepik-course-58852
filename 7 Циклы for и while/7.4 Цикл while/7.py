price = int(input())

count = 0

while price >= 25:
    count += 1
    price -= 25

while price >= 10:
    count += 1
    price -= 10

while price >= 5:
    count += 1
    price -= 5

while price >= 1:
    count += 1
    price -= 1

print(count)
