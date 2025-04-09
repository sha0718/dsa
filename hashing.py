nums = [1,2,3,4,5]
target = 8

nums_set = set(nums)
print(target in nums_set)  # Output: True


def count_frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

# Test
print(count_frequency([1, 2, 2, 3, 1, 4, 2]))  # Output: {1: 2, 2: 3, 3: 1, 4: 1}


#using collection.counter
from collections import Counter

arr= ([1, 2, 2, 3, 1, 4, 2])
freq = Counter(arr)
# Test
print(freq)  # Output: Counter({2: 3, 1: 2, 3: 1, 4: 1})