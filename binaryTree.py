class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
# Task 1
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)
# Task 2
def preorder_traversal(root):
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)
# Task 3
def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]


# Constructing the given binary tree
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(40)
root.left.right = TreeNode(20)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

# Task 4 Testing all traversal algorithms
inorder_result = inorder_traversal(root)
preorder_result = preorder_traversal(root)
postorder_result = postorder_traversal(root)


print("In-order Traversal Output:", inorder_result)
print("Pre-order Traversal Output:", preorder_result)
print("Post-order Traversal Output:", postorder_result)

# --Observations--
# ~ In-order Traversal visits the nodes in ascending order for a binary search tree.
# ~ Post-order Traversal visits all children nodes before their respective parent nodes.
# ~ Pre-order Traversal visits the root node first, followed by its left and right subtrees.