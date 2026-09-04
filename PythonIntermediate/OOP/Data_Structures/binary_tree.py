class Node:
    data : str
    next : 'Node'

    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    
class BinaryTree:
    root : Node

    def __init__(self, root):
        self.root = root

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        
        current_node = self.root
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    def print_tree(self, node, prefix="", is_left=True):
        if node is not None:
            if node.right is not None:
                self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(node.data))

            if node.left is not None:
                self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


#example usage of the BinaryTree class
print("\nCreating a binary tree with three nodes...\n")
tree = BinaryTree(Node(10))
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(8)
tree.insert(13)
tree.insert(15)
tree.insert(12)

tree.print_tree(tree.root)