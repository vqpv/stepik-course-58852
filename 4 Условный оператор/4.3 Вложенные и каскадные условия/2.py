a, b, c = int(input()), int(input()), int(input())

if a == b or b == c or a == c:
    if a == b and a == c:
        print("Равносторонний")
    else:
        print("Равнобедренный")
else:
    print("Разносторонний")
