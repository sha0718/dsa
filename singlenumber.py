def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test
print(single_number([4,1,2,1,2]))  # 4
print(single_number([2,2,1]))      # 1