from math import factorial


# объявление функции
def compute_b(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# считываем данные
_n = int(input())
_k = int(input())

# вызываем функцию
print(compute_b(_n, _k))
