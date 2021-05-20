# объявление функции
def is_valid_password(password):
    nums = password.split(':')
    flag_0 = False
    flag_1 = True

    if nums[0][:len(nums[0]) // 2] == nums[0][:-(len(nums[0]) // 2 + 1):-1]:
        flag_0 = True

    for i in range(2, int(int(nums[1]) * 0.5) + 1):

        if int(nums[1]) % i == 0:
            flag_1 = False
            break

    return bool(len(nums) == 3 and flag_0 and flag_1 and int(nums[2]) % 2 == 0)


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
