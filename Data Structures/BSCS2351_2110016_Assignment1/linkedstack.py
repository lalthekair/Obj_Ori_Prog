class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    # -------------------------- nested Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        def __init__(self, element, next):  # initialize node’s fields
            self._element = element  # reference to user’s element
            self._next = next

    # ------------------------------- stack methods -------------------------------
    def __init__(self):
        """Create an empty stack."""
        self.__head = None  # reference to the head node
        self.__size = 0  # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self.__size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self.__size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self.__head = self._Node(e, self.__head)  # create and link a new node
        self.__size += 1

    def top(self):
        """
           Return (but do not remove) the element at the top of the stack.
           Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            print("Error! Stack is Empty")
            return
        else:
            return self.__head._element  # top of stack is at head of list

    def pop(self):
        """
            Remove and return the element from the top of the stack (i.e., LIFO).
            Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            print("Error! Stack is Empty")
            return
        else:
            answer = self.__head._element
            self.__head = self.__head._next  # bypass the former top node
            self.__size -= 1
            return answer

####################################################
# added method list_stack_items(self)

    def list_stack_items(self):
        if self.is_empty():
            print("Nothing to list!")
        else:
            print("\nListing chairs of the stack...\nStack from Top to Bottom:")
            node = self.__head
            while node is not None:
                print(node._element)  # print element; not the address
                node = node._next
