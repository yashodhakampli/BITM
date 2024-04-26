class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    """
    Perform inorder traversal of the binary tree.
    
    Args:
    - root: The root node of the binary tree.
    
    Returns:
    - result: List containing the inorder traversal of the tree.
    """
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.val)
        result += inorder_traversal(root.right)
    return result

def preorder_traversal(root):
    """
    Perform preorder traversal of the binary tree.
    
    Args:
    - root: The root node of the binary tree.
    
    Returns:
    - result: List containing the preorder traversal of the tree.
    """
    result = []
    if root:
        result.append(root.val)
        result += preorder_traversal(root.left)
        result += preorder_traversal(root.right)
    return result

def postorder_traversal(root):
    """
    Perform postorder traversal of the binary tree.
    
    Args:
    - root: The root node of the binary tree.
    
    Returns:
    - result: List containing the postorder traversal of the tree.
    """
    result = []
    if root:
        result += postorder_traversal(root.left)
        result += postorder_traversal(root.right)
        result.append(root.val)
    return result

# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder traversal:", inorder_traversal(root))
print("Preorder traversal:", preorder_traversal(root))
print("Postorder traversal:", postorder_traversal(root))