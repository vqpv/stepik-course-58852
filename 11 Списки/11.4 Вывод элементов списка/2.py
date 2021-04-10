n = int(input())

func_res = []

for _ in range(n):
    x = int(input())
    func_res.append((x ** 2) + (2 * x) + 1)
    print(x)

print()
print(*func_res, sep='\n')
