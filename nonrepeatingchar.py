from collections import Counter

def first_unique_char(s):
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

print(first_unique_char("leetcode"))  # 0
print(first_unique_char("loveleetcode"))  # 2