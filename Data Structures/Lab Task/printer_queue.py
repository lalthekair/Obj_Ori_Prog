import random


class Node:

    def __init__(self, request_name, content, request_id, next_node=None):
        self.name = request_name
        self.id = request_id
        self.content = content
        self.next = next_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):  # print all nodes
        temp = self.head
        if temp is None:
            print("this list is empty")
            return
        while temp:
            print(temp.name, " ", temp.id, '\n', temp.content)
            temp = temp.next

    def list_len(self):  # count the nodes
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count



    def add_request(self, new_name, new_node):  # enqueue
        # should add to the tail of the list
        if self.head is None:
            self.tail = self.head = Node(new_name, new_node, random.randint(1000, 9999))
        else:
            temp = Node(new_name, new_node, random.randint(1000, 9999))
            self.tail.next = temp
            self.tail = temp

    def process_request(self):  # dequeue from the head of the list only
        if self.head:
            if self.head.next:
                print(str(self.head.id) + " request " + self.head.name + " is being printed\n", self.head.content)
                self.head = self.head.next
            else:
                print(str(self.head.id) + " request " + self.head.name + " is being printed\n", self.head.content)
                self.head = self.tail = None
        else:
            print("This list is empty.")
