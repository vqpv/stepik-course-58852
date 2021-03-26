num = int(input())

"""
a_list = list(range(97, 97 + num))
m_a_list = map(chr, a_list)

print(list(m_a_list))
"""

char_list = list(chr(a) for a in range(97, 97 + num))

print(char_list)
