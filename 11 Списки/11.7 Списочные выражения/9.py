nums = input()

print(*[int(num) ** 2 for num in nums.split() if int(num) % 2 == 0 and (int(num) ** 2) % 10 != 4])
