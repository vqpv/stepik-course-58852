n = int(input())

num_str1 = ""
num_str2 = ""

for i in range(n):
    num_str1 += str(i + 1)
    for j in reversed(range(i)):
        num_str2 += str(j + 1)

    print(num_str1 + num_str2)
    num_str2 = ""
