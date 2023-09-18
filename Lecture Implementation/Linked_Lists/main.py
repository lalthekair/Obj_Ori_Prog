"""
Create an application that stores the name and phone numbers for each person using linked list.
"""


class Node:
    def __init__(self, name, phone_num, next):
        self.name = name
        self.phone_num = phone_num
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_as_tail(self, name, num):
        new = Node(name, num, None) # at first, I will not add the address because I don't know it; None
        # step 1: create a node and store it in a variable
        # step 2:

    def add_as_head(self, name, num):
        if self.head is None:
            obj = Node(name, num, None)
            self.head = self.tail = obj
        else:
            # step 1 is to create a node and store it somewhere in a variable
            obj = Node(name, num, None)
            # step 2 is point the new node to the old head; create a reference between the new node and node #1
            # step 3 is point the head to this node;
            obj.next = self.head
            self.head = obj

    """def add_node_as_tail(self, name, num):
        obj2 = Node(name, num, None)
        self.tail = obj2

    def add_node_to_middle(self):
        pass"""


def main():
    lst = LinkedList()
    lst.add_as_head("Batool", 966556789)
    lst.add_as_head("Leena", 966453523)


main()