class Node:
    def __init__(self, data, is_root, left_child=None, right_child=None, parent=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.is_root = is_root
        self.parent = parent

    def is_the_root(self):
        return self.is_root

    def is_a_leaf(self):
        return self.right_child is None and self.left_child is None

    def has_left_child(self):
        return self.left_child is None

    def has_right_child(self):
        return self.right_child is None

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def add_left_child(self, left_data):
        if self.left_child is None:
            self.left_child = Node(left_data, False)
            self.left_child.parent = self

    def add_right_child(self, right_data):
        if self.right_child is None:
            self.right_child = Node(right_data, False)
            self.right_child.parent = self

    def set_node_data(self, new_data):
        self.data = new_data

    def get_node_data(self):
        return self.data

    def postorder(self, function):
        if self.left_child:
            self.left_child.postorder(function)
        if self.right_child:
            self.right_child.postorder(function)
        function(self)


class BinaryTree:
    def __init__(self):
        self.root = Node(None, True)

    def get_root(self):
        return self.root


tree = BinaryTree()
root = tree.get_root()
root.set_node_data(10)
root.add_left_child(9)
root.add_right_child(8)
node1 = root.get_left_child()
node1.add_left_child(7)
node1.add_right_child(6)


def print_data(node):
    print(node.get_node_data())

root.postorder(print_data)
