def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

# Test
weights = [1, 3, 4]
values = [15, 20, 30]
capacity = 4
print("Knapsack Max Value:", knapsack(weights, values, capacity))  # Output: 30
