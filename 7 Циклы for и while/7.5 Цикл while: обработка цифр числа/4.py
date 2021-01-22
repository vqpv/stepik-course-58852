num = int(input())

nums = []
summa = 0
proizv = 1

while num != 0:
    nums += str(num % 10)
    summa += num % 10
    proizv *= num % 10
    num = num // 10
​
print(summa)
print(len(nums))
print(proizv)
print(summa / len(nums))
print(nums[len(nums) - 1])
print(int(nums[len(nums) - 1]) + int(nums[0]))
