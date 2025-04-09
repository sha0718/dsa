def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1  # Length of unique part

# Test
arr = [1, 1, 2, 2, 3]
new_len = remove_duplicates(arr)
print(arr[:new_len])  # Output: [1, 2, 3]