# объявление функции
def number_to_words(num):
    nums_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    nums_2 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    nums_3 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    if num < 10:
        return nums_1[num - 1]

    elif 10 <= num <= 19:
        return nums_2[num % 10]

    elif 20 <= num <= 99:
        if num % 10 == 0:
            return nums_3[num // 10 - 2]
        else:
            return nums_3[num // 10 - 2] + " " + nums_1[num % 10 - 1]

    else:
        return "Введите число от 1 до 99"


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
