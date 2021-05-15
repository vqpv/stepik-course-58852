# объявление функции
def quick_merge(count):
    output_list = []

    for _ in range(count):
        output_list += [int(i) for i in input().split()]

    return sorted(output_list)


# считываем данные
n = int(input())

# вызываем функцию
print(*quick_merge(n))
