str_nums = input()

list_nums = list(map(int, str_nums.split()))

if len(list_nums) >= 2:
    list_min = min(list_nums)
    list_max = max(list_nums)
    list_min_index = list_nums.index(list_min)
    list_max_index = list_nums.index(list_max)
    list_nums[list_max_index], list_nums[list_min_index] = list_nums[list_min_index], list_nums[list_max_index]

print(*list_nums)
