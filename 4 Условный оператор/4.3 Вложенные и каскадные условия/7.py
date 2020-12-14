colour1 = input()
colour2 = input()

if colour1 in ("красный", "синий", "желтый") or colour2 in ("красный", "синий", "желтый"):
    if colour1 == colour2:
        print(colour1)
    else:
        if colour1 == "красный" or colour2 == "красный":
            if colour1 == "синий" or colour2 == "синий":
                print("фиолетовый")
            elif colour1 == "желтый" or colour2 == "желтый":
                print("оранжевый")
            else:
                print("ошибка цвета")
        elif colour1 == "синий" or colour2 == "синий":
            if colour1 == "желтый" or colour2 == "желтый":
                print("зеленый")
            else:
                print("ошибка цвета")
        else:
            print("ошибка цвета")
else:
    print("ошибка цвета")
