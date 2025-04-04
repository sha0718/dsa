def double_list(arr):

    return [x * 2 for x in arr]     

print(double_list([1, 2, 3]))
print(double_list([4, 5, 6]))


def largest_number(arr):

    return max(arr)

print(largest_number([1, 2, 3]))
print(largest_number([4, 5, 6]))

# prefix sum
def prefix_sum(arr):

    result = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        result[i + 1] = result[i] + arr[i]
    return result

print(prefix_sum([1, 2, 3]))    
print(prefix_sum([4, 5, 6]))

