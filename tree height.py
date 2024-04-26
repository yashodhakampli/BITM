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
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        
        # Return the height of the tree, which is the maximum height of its left and right subtrees plus 1 (for the current node)
        return max(left_height, right_height) + 1

# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

print("Height of the binary tree:", height(root))