class Stack:
    def __init__(self, capacity):
        self.__stack = [None] * capacity
        self.top = -1

    def len(self):
        return self.top + 1

    def isEmpty(self):
        return self.top == -1
        # if self.top == -1:
        # return true
        # else:
        # return false

    def isFull(self):
        # return self.len() == len(self.__stack)  # can use capacity instead of stack length
        if self.len() == len(self.__stack):
            return True
        else:
            return False

    def push(self, x):  # step 1, increment top by 1 - step 2, change the value of the index of the new top to x
        """if self.isFull():
            print("Stack is full.")
        else:
            self.top += 1
            self.__stack[self.top] = x"""
        if self.isFull() is False:
            self.top += 1
            self.__stack[self.top] = x
        # Order matters; otherwise, the code will not execute correctly
        else:
            print("Stack is full!")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            topItem = self.__stack[self.top]
            self.__stack[self.top] = None
            self.top -= 1
            return topItem

    def top(self):  # or peek, same function
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.__stack[self.top]  # return the top element

    def get_stack(self):
        return self.__stack
