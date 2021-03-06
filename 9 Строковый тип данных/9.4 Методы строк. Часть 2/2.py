string = input().lower()

adenine = 0
guanine = 0
cytosine = 0
timin = 0

for i in string:
    if i == "а":
        adenine += 1
    elif i == "г":
        guanine += 1
    elif i == "ц":
        cytosine += 1
    elif i == "т":
        timin += 1

print('Аденин:', adenine)
print('Гуанин:', guanine)
print('Цитозин:', cytosine)
print('Тимин:', timin)
