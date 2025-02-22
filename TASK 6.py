def bfs_without_queue(graph, start):
    visited = set()
    def visit(node):
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in graph.get(node, []):
                visit(neighbor)
    visit(start)

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs_with_queue(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        queue.extend(node.children)

if __name__ == "__main__":
   
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': [],
        'G': []
    }
    print("BFS Without Queue:")
    bfs_without_queue(graph, 'A')
   
    print("\nBFS With Queue:")
    root = Node('A')
    root.children.append(Node('B'))
    root.children.append(Node('C'))
    root.children[0].children.append(Node('D'))
    root.children[0].children.append(Node('E'))
    root.children[1].children.append(Node('F'))
    root.children[0].children[1].children.append(Node('G'))
    
    bfs_with_queue(root)
