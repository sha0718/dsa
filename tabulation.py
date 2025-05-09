def fib_tab(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print("Fibonacci Tabulation:", fib_tab(10))  # Output: 55
