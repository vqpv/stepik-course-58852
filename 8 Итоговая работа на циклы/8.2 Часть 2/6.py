n = int(input())

last_num = n % 10
out_1 = 0
out_2 = 0
out_3 = 0
out_4 = 0
out_5 = 1
out_6 = 0

while n != 0:
    num = n % 10
    if num == 3:
        out_1 += 1
    if num == last_num:
        out_2 += 1
    if num % 2 == 0:
        out_3 += 1
    if num > 5:
        out_4 += num
    if num > 7:
        out_5 *= num
    if (num == 0) or (num == 5):
        out_6 += 1
    n = n // 10

print(out_1)
print(out_2)
print(out_3)
print(out_4)
print(out_5)
print(out_6)
