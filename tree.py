class Node:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color  # 'red' or 'black'
        self.left = None
        self.right = None

    def is_red(self):
        return self.color == 'red'


class RedBlackTree:
    def __init__(self):
        self.root = None

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        right_child.color = node.color
        node.color = 'red'
        return right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        left_child.color = node.color
        node.color = 'red'
        return left_child

    def flip_colors(self, node):
        node.color = 'red'
        node.left.color = 'black'
        node.right.color = 'black'

    def add(self, key):
        self.root = self._add(self.root, key)
        self.root.color = 'black'  

    def _add(self, node, key):
        if node is None:
            return Node(key, 'red')  

        if key < node.key:
            node.left = self._add(node.left, key)
        elif key > node.key:
            node.right = self._add(node.right, key)
        else:
            return node  

        if node.right and node.right.is_red() and not (node.left and node.left.is_red()):
            node = self.rotate_left(node) 

        if node.left and node.left.is_red() and node.left.left and node.left.left.is_red():
            node = self.rotate_right(node) 

        if node.left and node.left.is_red() and node.right and node.right.is_red():
            self.flip_colors(node)

        return node

tree = RedBlackTree()

elements = [20, 15, 25, 10, 18, 30, 5, 12]
for elem in elements:
    tree.add(elem)

def print_tree(node, indent="", position="root"):
    if node is not None:
        print(f"{indent} [{position}] Key: {node.key}, Color: {node.color}")
        print_tree(node.left, indent + "   ", position="L")
        print_tree(node.right, indent + "   ", position="R")

print_tree(tree.root)
