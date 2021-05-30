# объявление функции
def is_magic(date):
    d_nums = date.split(".")

    if int(d_nums[1][0]) == 0:
        month = int(d_nums[1][1])
    else:
        month = int(d_nums[1])

    return bool(int(d_nums[0]) * month == int(d_nums[2]) % 100)


# считываем данные
_date = input()

# вызываем функцию
print(is_magic(_date))
