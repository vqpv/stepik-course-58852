num = int(input())

nums = []

while num != 0:
    nums += str(num % 10)
    num = num // 10

print(f"Максимальная цифра равна {max(nums)}")
print(f"Минимальная цифра равна {min(nums)}")
