def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Test
print(fib(6))  # Output: 8
print(fib(10))  # Output: 55

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(fib_memo(15))  # Fast!
