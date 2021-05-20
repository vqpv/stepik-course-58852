# объявление функции
def is_palindrome(text):
    word_list = ''

    for i in text:
        if i not in [' ', ',', '.', '!', '?', '-']:
            word_list += i.lower()
    return bool(word_list[:(len(word_list) // 2)] == word_list[:-(len(word_list) // 2 + 1):-1])


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
