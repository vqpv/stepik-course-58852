ip = input()

check = 0

for num in ip.split('.'):
    if 0 <= int(num) <= 255:
        check += 1

if check == 4:
    print('ДА')

else:
    print('НЕТ')
