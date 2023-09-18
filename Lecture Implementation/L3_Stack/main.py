"""
Stacks are LIFO.
Pop will pop the first element
Push parameter is the element you want to add, push = append
"""


class Stack:
    def __init__(self, lst):
        self.lst = []

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        removed_value = self.lst.pop()  # pop is a built-in function that removes the last element
        """
        index = len(self.lst) - 1
        popped = self.lst[index]
        del self.lst[index]
        return popped
        """
        return removed_value


def main():
    stk = Stack([])
    stk.push(4)
    stk.push(3)
    print(stk.lst)  # printing stk alone will return memory location
    stk.pop()
    print(stk.lst)
    print("The removed element is", stk.pop())
    print(stk.lst)


main()
