n = input()

strings = []

for _ in range(int(n[1:])):
    string = input()

    if '#' in string:
        split_string = string.split('#')
        strings.append(split_string[0].rstrip())
    else:
        strings.append(string.rstrip())

print(*strings, sep='\n')
