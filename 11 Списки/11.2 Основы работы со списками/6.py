rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

for index, colour in enumerate(rainbow):
    if colour == "Green":
        rainbow[index] = "Зеленый"
    elif colour == "Violet":
        rainbow[index] = "Фиолетовый"

print(rainbow)
