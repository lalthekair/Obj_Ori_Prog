class Node:
    # this class is created to add/create nodes
    # everytime we add a node, simply create an object from class Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    # in this class, we will add all the methods to manage our tree
    # add method, search method, print elements, etc.
    # inserting into the tree

    """def __init__(self):
        self.head = None

    def insert(self, root, value):
        if self.head is None:
            self.head = Node(value)
        else:
            pass"""

    def insert(self, root, new_value):
        # case 1: if root is None (tree is empty)
        if root.data is None:
            root = Node(new_value)
            return root

        # case 2: new_Value is greater than the root
        elif root.data < new_value:
            root.right = self.insert(root.right, new_value)
        """elif root < new_value:
            root.right = new_value"""

        # case 3: new_value is less than the root
        else:
            root.left = self.insert(root.left, new_value)

        """elif root > new_value:
            root.left = new_value
            return root"""


def main():
    root = BinarySearchTree
    root.insert(root, 20)


main()