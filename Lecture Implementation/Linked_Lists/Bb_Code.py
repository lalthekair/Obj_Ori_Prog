class Node:

    def __init__(self, name, Tel, next_node=None):
        self.name = name
        self.Tel = Tel
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
            print(temp.name, " ", temp.Tel)
            temp = temp.next

    def search(self, s_name):  # search for a node and return Ref. Or Pointer
        temp = self.head
        if temp is None:
            print("this list is empty ")
            return
        while temp:
            if temp.name == s_name:
                print(temp.name, "'s phone number is", temp.Tel)
                print(temp)  # this prints the memory address of the node
                return temp
            temp = temp.next
            if temp is None:
                print(s_name + "  is not in the list!")

    def list_len(self):  # count the nodes
        count = 0
        temp = self.head  # using a temporary variable to avoid messing up the list in any way
        while temp:
            count += 1
            temp = temp.next
        return count

    def add_node_as_head(self, name, tel):  # add from head side
        if self.head is None:
            self.tail = self.head = Node(name, tel, None)  # first node
        else:
            temp = Node(name, tel, None)
            temp.next = self.head  # link the new node
            self.head = temp  # update the head

    def add_node_as_tail(self, name, tel):  # Add from tail side
        if self.head is None:
            self.tail = self.head = Node(name, tel, None)  # first node
        else:
            temp = Node(name, tel, None)
            self.tail.next = temp  # link the new node
            self.tail = temp  # update the tail

    def add_node_after(self, name, tel, R_node):  # add in the middle after a node
        temp = Node(name, tel, None)
        temp.next = R_node.next
        R_node.next = temp

    def delete_node(self, S_name):
        if self.head is None:
            print(" this list is empty")
            return

        my_node = self.head
        prev_node = self.head
        while my_node:
            if my_node.name == S_name:  # check each node one by one if it matches the required node

                if self.head == my_node:  # case 1: we remove the first node
                    if self.head.next is None:  # case 1a: it is the first and only node
                        self.head = None
                        self.tail = None
                    else:  # case 1b: it's the head but not the only node
                        self.head = my_node.next

                elif self.tail == my_node:  # case 2: we remove the last node
                    self.tail = prev_node
                    prev_node.next = None

                else:  # case 3: we delete from the middle
                    prev_node.next = my_node.next

                print(my_node.name + " is deleted")
                return

            prev_node = my_node  # if I didn't find the element, I will move on to the next one
            my_node = my_node.next
        print(S_name + " is not in the list!")
        return


def main():
    ll = LinkedList()
    ll.add_node_as_tail("dua", 444)
    ll.add_node_as_tail("alaa", 5555)
    ll.add_node_as_tail("anood", 1234)
    ll.printList()
    print("1-->")
    xx = ll.search("anood")
    yy = ll.search("alaa")
    print(ll.list_len())
    ll.add_node_as_head("loay", 1111)
    ll.add_node_as_head("hamody", 1111)
    ll.add_node_as_tail("loay", 22222222222)
    ll.add_node_as_tail("loay", 3333333333333)
    ll.add_node_as_tail("stooop", 55)
    ll.add_node_after("my_node_mid", 77, yy)
    ll.printList()
    print(ll.list_len())
    ll.delete_node("stooop")
    ll.delete_node("anood")
    print(ll.list_len())
    ll.printList()


main()