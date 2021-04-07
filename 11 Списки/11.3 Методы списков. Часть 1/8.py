n = int(input())

input_list = []

for _ in range(n):
    input_list.append(input())

k = int(input())

for word in input_list:
    if len(word) >= k:
        print(word[k - 1], end="")
