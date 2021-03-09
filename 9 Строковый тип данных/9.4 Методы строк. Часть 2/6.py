string = input()

char_count = 0
m_char = ""

for char in string:
    if string.count(char) >= char_count:
        char_count = string.count(char)
        m_char = char

print(m_char)
