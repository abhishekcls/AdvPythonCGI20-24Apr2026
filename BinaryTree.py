class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val,end=" ")


# Create Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Test
print("Inorder:")
inorder(root)#Left Root Right -> 2 1 3

print("\nPreorder:")
preorder(root)#Root Left Right -> 1 2 3

print("\nPostorder:")
postorder(root)#Left Right Root -> 2 3 1