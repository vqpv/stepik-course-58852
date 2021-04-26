n = int(input())

numbers = [num ** 2 for num in range(1, n + 1)]

print(*numbers, sep='\n')
