n = int(input())

num = []

for i in range(n):
    num.append(int(input()))

print(max(num))
num.remove(max(num))
print(max(num))
