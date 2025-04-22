def max_sum(arr, k):
    n = len(arr)
    max_sum = curr_sum = sum(arr[:k])
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum  

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 4
print(max_sum(arr, k))      
