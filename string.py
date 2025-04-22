s = "hello world"

print(s[0])       # 'h'
print(s[-1])      # 'd'
print(s[0:5])     # 'hello'
print(s.upper())  # 'HELLO WORLD'
print(s.split())  # ['hello', 'world']
print(s.replace("world", "Python"))  # 'hello Python'
print(len(s))     # 11
print(s.count("o"))  # 2
print(s.find("o"))   # 4
print(s[::-1])