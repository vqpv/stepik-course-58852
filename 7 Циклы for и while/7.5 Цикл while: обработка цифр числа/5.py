num = int(input())

nums = []

while num != 0:
    nums += str(num % 10)
    num = num // 10

print(nums[len(nums) - 2])
