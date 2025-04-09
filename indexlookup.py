def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i

# Test
print(two_sum([2, 7, 11, 15], 26))  # Output: [0, 1]
print(two_sum([3, 2, 4], 6))       # Output: [1, 2]