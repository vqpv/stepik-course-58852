nums = input()

nums_list = nums.split()
count = 0

for i, n in enumerate(nums_list):
    for m in nums_list[i + 1: len(nums_list)]:
        if n == m:
            count += 1

print(count)
