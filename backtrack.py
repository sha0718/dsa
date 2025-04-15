def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])  # add a copy of current path
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # backtrack

    backtrack(0, [])
    return result

# Test
print(subsets([1, 2, 3]))
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]