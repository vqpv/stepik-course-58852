# объявление функции
def print_fio(n, s, p):
    print(s[0].upper() + n[0].upper() + p[0].upper())


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
