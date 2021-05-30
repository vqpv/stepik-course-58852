# объявление функции
def is_pan(text):
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in text.lower():
            return False

    return True


# считываем данные
_text = input()

# вызываем функцию
print(is_pan(_text))
