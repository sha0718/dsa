def subsets(nums):
    result = []
    n = len(nums)
    for mask in range(1 << n):  # 2^n subsets
        subset = []
        for i in range(n):
            if (mask >> i) & 1:
                subset.append(nums[i])
        result.append(subset)
    return result

# Test
print(subsets([1, 2, 3]))
