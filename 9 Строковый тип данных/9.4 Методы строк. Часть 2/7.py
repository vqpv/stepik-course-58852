string = input()

if string.find('f') != -1 and string.rfind('f') != -1:
    if string.find('f') != string.rfind('f'):
        print(string.find('f'), string.rfind('f'))
    else:
        print(string.find('f'))
else:
    print("NO")
