num = int(input())

div_list = []

for i in range(1, num + 1):
    if num % i == 0:
        div_list.append(i)

print(div_list)
