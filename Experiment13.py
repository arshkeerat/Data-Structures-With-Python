# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Create the root node
root = Node(8)
# Create child nodes
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left=Node(4)
root.left.right.right=Node(7)
root.right.right=Node(14)
root.right.right.left=Node(13)
# Display the tree
print("Root:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)
print("Left child of 3 :", root.left.left.data)
print("Right child of 3:", root.left.right.data)
print("Left child of 6:", root.left.right.left.data)
print("Right child of 6:", root.left.right.right.data)
print("Right child of 10:", root.right.right.data)
print("Left child of 14:" ,root.right.right.left.data)

from collections import deque

# Create the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Preorder Traversal (Root, Left, Right)
def preorder(root):
    if not root:
        return
    stack = deque([root])
    while stack:
        node = stack.pop()
        print(node.data, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Inorder Traversal (Left, Root, Right)
def inorder(root):
    stack = deque()
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.data, end=" ")
        current = current.right

# Postorder Traversal (Left, Right, Root)
def postorder(root):
    if not root:
        return
    stack = deque([root])
    output = deque() 
    while stack:
        node = stack.pop()
        output.appendleft(node.data)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    for data in output:
        print(data, end=" ")

# Perform tree traversals
print("Preorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
postorder(root)