# объявление функции
def is_password_good(password):
    return bool(len(password) >= 8 and password != password.upper() and password != password.lower() and not password.isdigit() and not password.isalpha() and password.isalnum())


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
