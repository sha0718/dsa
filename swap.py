def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

# Test
print(swap(3, 7))  # (7, 3)
print(swap(10, 20))  # (20, 10)