string = input()

vowels = "ауоыиэяюёеАУОЫИЭЯЮЁЕ"
consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"

vow_count = 0
con_count = 0

for char in string:
    if char in vowels:
        vow_count += 1
    elif char in consonants:
        con_count += 1

print(f'Количество гласных букв равно {vow_count}')
print(f'Количество согласных букв равно {con_count}')
