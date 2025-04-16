class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def update(self, i, val):
        pos = i + self.n
        self.tree[pos] = val
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
    
    def query(self, l, r):  # sum in range [l, r)
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

# Test
st = SegmentTree([1, 3, 5, 7, 9, 11])
print("Range Sum (1,4):", st.query(1, 4))  # Output: 15 (3+5+7)
st.update(1, 10)
print("Range Sum (1,4) after update:", st.query(1, 4))  # Output: 22

