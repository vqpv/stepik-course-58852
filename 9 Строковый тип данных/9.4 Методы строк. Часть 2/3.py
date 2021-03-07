n = int(input())

string_count = 0

for i in range(n):
    if input().count("11") >= 3:
        string_count += 1

print(string_count)
