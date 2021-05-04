nums = input().split()

print('+'.join(nums), '=', sum(list(map(int, nums))), sep='')
