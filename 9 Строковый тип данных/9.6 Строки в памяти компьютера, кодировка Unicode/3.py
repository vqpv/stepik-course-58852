shift = int(input())
string = input()

for char in string:
    if ord(char) - shift < 97:
        print(chr(122 - (96 - (ord(char) - shift))), end="")
    else:
        print(chr(ord(char) - shift), end="")
