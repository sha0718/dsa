def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

# Test
print(is_valid("()[]{}"))    # True
print(is_valid("([)]"))      # False
print(is_valid("{[]}"))      # True