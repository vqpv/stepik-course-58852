nums_list = list(map(int, input().split()))

print(*sorted(nums_list))
print(*sorted(nums_list, reverse=True))
