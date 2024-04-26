class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def height(root):
    """
    Calculate the height of the binary tree.
    
    Args:
    - root: The root node of the binary tree.
    
    Returns:
    - height: The height of the binary tree.
    """
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def is_balanced(root):
    """
    Check if the binary tree is balanced.
    
    Args:
    - root: The root node of the binary tree.
    
    Returns:
    - balanced: True if the binary tree is balanced, False otherwise.
    """
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    # Check if the height difference between the left and right subtrees is <= 1
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    
    return False

# Example usage:
# Constructing a balanced binary tree
balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(3)
balanced_root.left.left = TreeNode(4)
balanced_root.left.right = TreeNode(5)

# Constructing an unbalanced binary tree
unbalanced_root = TreeNode(1)
unbalanced_root.left = TreeNode(2)
unbalanced_root.right = TreeNode(3)
unbalanced_root.left.left = TreeNode(4)
unbalanced_root.left.left.left = TreeNode(5)

print("Is the balanced binary tree balanced?", is_balanced(balanced_root))
print("Is the unbalanced binary tree balanced?", is_balanced(unbalanced_root))