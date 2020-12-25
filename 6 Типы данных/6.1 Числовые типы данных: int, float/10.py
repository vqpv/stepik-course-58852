num = int(input())

a1 = num // 100
a2 = (num // 10) % 10
a3 = num % 10

sum_num = a1 + a2 + a3

if max(a1, a2, a3) - min(a1, a2, a3) == sum_num - max(a1, a2, a3) - min(a1, a2, a3):
    print("Число интересное")
else:
    print("Число неинтересное")
