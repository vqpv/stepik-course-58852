# объявление функции
def draw_box():
    for i in range(14):
        for j in range(10):
            if i in (0, 13):
                print('*', end='')
            elif j in (0, 9):
                print('*', end='')
            else:
                print(' ', end='')
        print()

# основная программа
draw_box()  # вызов функции
