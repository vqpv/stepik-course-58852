string = input()

print(string[:string.find('h')] + string[string.rfind('h'):string.find('h'):-1] + string[string.rfind('h'):])
