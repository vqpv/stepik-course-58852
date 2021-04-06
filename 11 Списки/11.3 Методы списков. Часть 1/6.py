count = int(input())

input_list = []
sum_list = []

for _ in range(count):
    input_list.append(int(input()))

for index in range(len(input_list) - 1):
    sum_list.append(input_list[index] + input_list[index + 1])

print(sum_list)

"""
count, a = int(input()), int(input())

sum_list = []

for _ in range(count - 1):
    b = int(input())
    sum_list.append(a + b)
    a = b
    
print(sum_list)
"""