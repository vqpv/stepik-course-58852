word = input()
count = 0

while word != "стоп" and word != "хватит" and word != "достаточно":
    word = input()
    count += 1

print(count)
