# объявление функции
def draw_triangle(fill, base):
    for i in range(base):
        r = (base // 2 + 1) - abs(base // 2 - i)
        print(fill * r)


# считываем данные
f = input()
b = int(input())

# вызываем функцию
draw_triangle(f, b)
