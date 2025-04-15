a = [1, 2, 3]
b = a
print(a == b)  # True
print(a is b)  # True (same object)

x = 10
print(type(x))  # <class 'int'>


lst = [1, 2, 2, 3, 4, 4]
unique_lst = list(set(lst))  # [1, 2, 3, 4]
print(unique_lst)  # [1, 2, 3, 4]

a, b = 5, 10
a, b = b, a
print(a, b)  # 10, 5


my_dict = {'name': 'Alice', 'age': 25}
if 'age' in my_dict:
    print("Key exists")

lst = [1, 2, 3, 4]
lst.pop(2)  # Removes index 2 (value 3)
lst.remove(4)  # Removes value 4
print(lst)  # [1, 2]

names = ['Alice', 'Bob']
ages = [25, 30]
zipped = list(zip(names, ages))  # [('Alice', 25), ('Bob', 30)]
print(zipped)  # [('Alice', 25), ('Bob', 30)]

add = lambda x, y: x + y
print(add(2, 3))  # 5


import copy
lst1 = [[1, 2], [3, 4]]
lst2 = copy.deepcopy(lst1)
lst2[0][0] = 99  # Doesn't affect lst1
print(lst1)  # [[1, 2], [3, 4]]
print(lst2)  # [[99, 2], [3, 4]]

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


def decorator(func):
    def wrapper():
        print("Before function call")
        func()
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
print(squares)

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

def example_function(*args, **kwargs):
    print(args)   # Tuple of arguments
    print(kwargs) # Dictionary of keyword arguments

example_function(1, 2, 3, name="Alice", age=25)


import math
print(math.sqrt(16))  # 4.0

dict1 = {'a': 1}
dict2 = {'b': 2}
merged = dict1 | dict2  # {'a': 1, 'b': 2}
print(merged)  # {'a': 1, 'b': 2}

class Example:
    @staticmethod
    def static_method():
        print("Static method")

    @classmethod
    def class_method(cls):
        print("Class method")

Example.static_method()
Example.class_method()

# import gc
# gc.collect()  # Forces garbage collection

# with open('file.txt', 'r') as f:
#     content = f.read()
#     print(content)

# with open('file.txt', 'w') as f:
#     f.write("Hello, World!")

A = {1, 2, 3}
B = {2, 3, 4}
print(A | B)  # {1, 2, 3, 4}
print(A & B)  # {2, 3}

from functools import reduce

nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nums)))  # [2, 4, 6, 8]
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]
print(reduce(lambda x, y: x + y, nums))  # 10


class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Creating class", name)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True

class Examples:
    def method(self):
        return "Original"

def patched_method(self):
    return "Patched"

Examples.method = patched_method
obj = Examples()
print(obj.method())  # Patched

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

for num in Counter(1, 5):
    print(num)  # 1, 2, 3, 4


# import cProfile
# cProfile.run('sum(range(1000))')

# import threading
# t = threading.Thread(target=print, args=("Hello",))
# t.start()


# import multiprocessing
# p = multiprocessing.Process(target=print, args=("World",))
# p.start()


