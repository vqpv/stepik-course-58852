# объявление функции
def get_next_prime(num):
    flag = True

    while flag:
        num += 1
        flag = False

        for i in range(2, int(num * 0.5) + 1):
            if num % i == 0:
                flag = True
                break

    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
