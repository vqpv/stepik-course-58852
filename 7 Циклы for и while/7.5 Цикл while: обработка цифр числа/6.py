num = int(input())

nums = []

while num != 0:
    nums += str(num % 10)
    num = num // 10

if max(nums) == min(nums):
    print("YES")
else:
    print("NO")
