string = input()

lower_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
upper_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
words = string.split()
cipher_words = []

for word in words:
    new_word = ''
    count = 0

    for char in word:
        if char in lower_alphabet or char in upper_alphabet:
            count += 1

    for char in word:
        if char in lower_alphabet:
            new_word += lower_alphabet[(lower_alphabet.index(char) + count) % 26]
        elif char in upper_alphabet:
            new_word += upper_alphabet[(upper_alphabet.index(char) + count) % 26]
        else:
            new_word += char
    cipher_words.append(new_word)

print(' '.join(cipher_words))
