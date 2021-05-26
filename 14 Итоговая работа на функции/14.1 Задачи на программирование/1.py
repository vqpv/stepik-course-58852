# объявление функции
def draw_triangle():
    for i in range(8):
        print(" " * (8 - 1 - i) + "*" * (i * 2 + 1), sep="")


# основная программа
draw_triangle()  # вызов функции
