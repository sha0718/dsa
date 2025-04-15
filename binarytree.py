class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def depth(root, val, level=0):
    if not root:
        return -1
    if root.val == val:
        return level
    left = depth(root.left, val, level + 1)
    if left != -1:
        return left
    return depth(root.right, val, level + 1)

def diameter(root):
    dia = 0
    def dfs(node):
        nonlocal dia
        if not node:
            return 0
        lh = dfs(node.left)
        rh = dfs(node.right)
        dia = max(dia, lh + rh)
        return 1 + max(lh, rh)
    
    dfs(root)
    return dia


# Build a tree
root = None
for val in [10, 5, 15, 2, 7, 12, 20]:
    root = insert_bst(root, val)

# Traversals
print("Inorder:", end=' ')
inorder(root)  # 2 5 7 10 12 15 20

print("\nPreorder:", end=' ')
preorder(root)  # 10 5 2 7 15 12 20

print("\nPostorder:", end=' ')
postorder(root)  # 2 7 5 12 20 15 10

# Tree Properties
print("\nHeight:", height(root))         # 3
print("Depth of 7:", depth(root, 7))     # 2
print("Diameter:", diameter(root))       # 4


