string = input()

print(string[0:string.find('h')] + string[string.rfind('h') + 1: len(string)])
