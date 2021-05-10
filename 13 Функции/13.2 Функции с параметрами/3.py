# объявление функции
def print_digit_sum(num):
    print(sum(int(i) for i in num))


# считываем данные
n = input()

# вызываем функцию
print_digit_sum(n)
