# объявление функции
def find_all(target, symbol):
    symbol_index = []

    for index, character in enumerate(target):
        if symbol == character:
            symbol_index.append(index)
    return symbol_index


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
