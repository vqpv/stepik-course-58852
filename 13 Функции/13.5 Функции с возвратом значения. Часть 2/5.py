# объявление функции
def is_one_away(word1, word2):
    count = 0

    for i, _ in enumerate(word1):
        if word1[i] == word2[i]:
            count += 1
    return bool(count == len(word1) - 1)


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
