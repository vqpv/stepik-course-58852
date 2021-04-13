n = int(input())

nums_list_minus = []
nums_list_zero = []
nums_list_plus = []

for _ in range(n):
    num = int(input())
    if num < 0:
        nums_list_minus.append(num)
    elif num == 0:
        nums_list_zero.append(num)
    elif num > 0:
        nums_list_plus.append(num)

print(*nums_list_minus, sep='\n')
print(*nums_list_zero, sep='\n')
print(*nums_list_plus, sep='\n')
