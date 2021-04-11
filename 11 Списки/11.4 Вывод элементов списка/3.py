n = int(input())

n_list = []

for _ in range(n):
    n_list.append(int(input()))

del n_list[n_list.index(min(n_list))]
del n_list[n_list.index(max(n_list))]

print(*n_list, sep='\n')
