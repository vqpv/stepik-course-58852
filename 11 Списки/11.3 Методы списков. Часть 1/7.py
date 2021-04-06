count = int(input())

num_list = []

for _ in range(count):
    num_list.append(int(input()))

del num_list[1::2]

print(num_list)
