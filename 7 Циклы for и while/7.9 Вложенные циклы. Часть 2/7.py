num_1, num_2 = int(input()), int(input())

for i in range(num_1, num_2 + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
