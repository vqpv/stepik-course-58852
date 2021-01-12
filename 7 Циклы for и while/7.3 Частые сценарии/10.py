count = 0

for num in range(10):
    if int(input()) % 2 == 0:
        count += 1

if count == 10:
    print("YES")
else:
    print("NO")
