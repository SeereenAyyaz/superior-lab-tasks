class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_with_stack(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')

if __name__ == "__main__":
    root = Node(7)
    root.left = Node(8)
    root.right = Node(1)
    root.left.left = Node(0)
    root.left.right = Node(3)
    root.right.left = Node(9)
    root.right.right = Node(6)
    
    print("DFS with Stack:")
    dfs_with_stack(root)
    print("\nInorder Traversal:")
    inorder_traversal(root)
    print("\nPreorder Traversal:")
    preorder_traversal(root)
    print("\nPostorder Traversal:")
    postorder_traversal(root)
