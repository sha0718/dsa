def next_greater_elements(nums):
    res = [-1] * len(nums)
    stack = []  # store indices

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            res[index] = nums[i]
        stack.append(i)
    return res

# Test
print(next_greater_elements([2, 1, 2, 4, 3]))  # [4, 2, 4, -1, -1]
