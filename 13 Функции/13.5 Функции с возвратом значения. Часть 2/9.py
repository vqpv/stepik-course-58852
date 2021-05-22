# объявление функции
def convert_to_python_case(text):
    snake_string = ""
    for i, j in enumerate(text):
        if i != 0 and j.isupper():
            snake_string += '_' + j.lower()
        else:
            snake_string += j.lower()
    return snake_string


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
