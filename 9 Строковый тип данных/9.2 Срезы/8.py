string = input()

len_s = len(string)

print(string[((len_s + 1) // 2):len_s], string[0:((len_s + 1) // 2)], sep='')
