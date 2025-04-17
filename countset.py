def count_bits(n):
    count = 0
    while n:
        n &= (n - 1)  # clear the lowest set bit
        count += 1
    return count

# Test
print(count_bits(13))  # 3 (binary: 1101)
print(count_bits(7))   # 3 (binary: 111)