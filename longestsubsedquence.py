def lis(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

# Test
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("LIS Length:", lis(nums))  # Output: 4 (2, 3, 7, 101)
