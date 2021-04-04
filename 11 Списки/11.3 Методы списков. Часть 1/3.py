alphabet_list = []
count = 0

for i in range(97, 123):
    count += 1
    alphabet_list.append(chr(i) * count)

print(alphabet_list)
