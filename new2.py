import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())


class Sample:
    def __str__(self):
        return "This is a sample object"

obj = Sample()
print(obj)  # Calls __str__()

# import gc
# gc.collect()  # Forces garbage collection

import pickle

data = {"name": "Alice", "age": 25}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)  # {'name': 'Alice', 'age': 25}

import weakref

class Example:
    pass

obj = Example()
weak_ref = weakref.ref(obj)

print(weak_ref())  # Returns object
del obj
print(weak_ref())  # None (garbage collected)

def add(x: int, y: int) -> int:
    return x + y

print(add(1, 2))


from functools import lru_cache

@lru_cache(maxsize=100)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Cached results speed up execution

class Examples:
    __slots__ = ['name', 'age']  # Prevents adding new attributes

obj = Examples()
obj.name = "Alice"
# obj.address = "New York"  # AttributeError

# class MyError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)

# raise MyError("Custom error occurred")

import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(greet())

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 25)
print(p)  # Person(name='Alice', age=25)

import cProfile
cProfile.run('sum(range(1000000))')

def multiply(a: int, b: int) -> int:
    return a * b

# module_a.py
import module_b
def func_a():
    module_b.func_b()

# module_b.py
import module_a
def func_b():
    module_a.func_a()





