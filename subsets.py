def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])  # Add a copy
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # undo

    backtrack(0, [])
    return result

# Test
print("Subsets:", subsets([1, 2, 3]))
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
# This code generates all subsets of a given list of numbers using backtracking.