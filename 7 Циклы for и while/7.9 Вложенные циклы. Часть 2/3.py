num1, num2 = int(input()), int(input())

list_divisors = []
list_sum_divisors = []

for i in range(num1, num2 + 1):
    count_divisors = 0
    sum_divisors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count_divisors += 1
            sum_divisors += j
    list_divisors.append(count_divisors)
    list_sum_divisors.append(sum_divisors)

for jj in reversed(range(len(list_sum_divisors))):
    if max(list_sum_divisors) == list_sum_divisors[jj]:
        print(jj + num1, max(list_sum_divisors))
        break
