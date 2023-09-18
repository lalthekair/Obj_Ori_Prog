class Stack:

    def __init__(self):
        self.__lst = []  # A list is initiated with unlimited length

    def push(self, value):
        self.__lst.append(value)

    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        return self.__lst.pop()

    def len(self):
        return len(self.__lst)

    def top(self):
        if self.isEmpty():
            return "The stack is empty"
        return self.__lst[-1]  # We are starting from the right (top), so -1

    def isEmpty(self):
        return self.len() == 0  # Returns a boolean value if the length is = 0 true, else false

    # def __str__(self):
        # print(self.__lst)
        # I don't know why this throws an error
