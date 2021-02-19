string = input()

text = "Цифр нет"

for char in string:
    if char.isdigit():
        text = "Цифра"

print(text)
