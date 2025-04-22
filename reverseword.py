def reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())

print(reverse_words("hello world"))  # "olleh dlrow"
print(reverse_words("Python is fun"))  # "nohtyP si nuf"