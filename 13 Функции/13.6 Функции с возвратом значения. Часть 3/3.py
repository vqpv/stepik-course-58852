import math


# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c

    if d == 0:
        return -b / (2 * a), -b / (2 * a)

    elif d > 0:
        x_1 = (-b + math.sqrt(d)) / (2 * a)
        x_2 = (-b - math.sqrt(d)) / (2 * a)
        return min(x_1, x_2), max(x_1, x_2)

    else:
        return "Корней нет!"


# считываем данные
_a, _b, _c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(_a, _b, _c)
print(x1, x2)
