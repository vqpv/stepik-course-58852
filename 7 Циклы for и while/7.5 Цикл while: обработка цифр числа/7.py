num = int(input())

nums = []
answer = 0

while num != 0:
    nums += str(num % 10)
    num = num // 10

for i in range(len(nums) - 1):
    if nums[i] <= nums[i + 1]:
        answer = answer
    else:
        answer += 1

if answer == 0:
    print("YES")
else:
    print("NO")

