num1 = int(input())
num2 = int(input())
char_inp = input()

if char_inp == "+":
    print(num1 + num2)

elif char_inp == "-":
    print(num1 - num2)

elif char_inp == "*":
    print(num1 * num2)

elif char_inp == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("На ноль делить нельзя!")
else:
    print("Неверная операция")
