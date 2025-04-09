def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return True
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return False

# Test
print(has_pair_with_sum([1, 2, 3, 4, 6], 6))  # True (2+4)
print(has_pair_with_sum([1, 2, 3, 9], 8))     # False
