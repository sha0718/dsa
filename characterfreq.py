from collections import Counter

def char_freq(s):
    return Counter(s)

print(char_freq("banana"))  # Counter({'a': 3, 'n': 2, 'b': 1})
print(char_freq("hello world"))  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
