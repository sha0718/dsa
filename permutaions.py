def permute(nums):
    result = []
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if i in used:
                continue
            used.add(i)
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used.remove(i)

    backtrack([], set())
    return result

# Test
print("Permutations:", permute([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# This code generates all permutations of a given list of numbers using backtracking.
