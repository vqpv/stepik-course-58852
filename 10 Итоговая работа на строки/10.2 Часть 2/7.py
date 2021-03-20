string = input()

for index, char in enumerate(string):
    if index % 3 != 0:
        print(char, end="")
