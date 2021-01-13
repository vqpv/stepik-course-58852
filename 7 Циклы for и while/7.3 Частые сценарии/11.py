count_nums = int(input())

fib_nums = [1, 1]

if count_nums == 1:
    result = "1"
else:
    result = "1 1 "

for i in range(2, count_nums):
    fib_nums.append(fib_nums[i - 2] + fib_nums[i - 1])
    result += str(fib_nums[i]) + " "

print(result)
