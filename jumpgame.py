def can_jump(nums):
    reach = 0
    for i, num in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + num)
    return True

print("Can Jump:", can_jump([2,3,1,1,4]))  # Output: True
