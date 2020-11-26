num = input()

summa = 0
proizv = 1

for i in num:
    summa += int(i)
    proizv *= int(i)

print(f"Сумма цифр = {summa}")
print(f"Произведение цифр = {proizv}")
