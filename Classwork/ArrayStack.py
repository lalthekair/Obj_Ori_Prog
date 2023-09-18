class ArrayStack:

    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.top = -1


    def size(self):
        return self.top + 1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        #return self.top == -1

    def isFull(self):
        if self.size() == len(self.stack):
            return True
        else:
            return False
    #return     self.size() == len(self.stack)

    def push(self, x):
        if self.isFull() == False:
            self.top += 1
            self.stack[self.top] = x

    def pop(self):
        if self.isEmpty() == False:
            x = self.stack[self.top]
            self.stack[self.top] = None
            self.top -=1
            return x
        else:
            return "Empty stack"

    def peek(self):
        if self.isEmpty() == False:
            return self.stack[self.top]
        else:
            "Empty stack"





def main():
    stk = ArrayStack(5)
    print(stk.isEmpty())
    print(stk.pop())
    print("I will push 5")
    stk.push(5)
    print(stk.isEmpty())
    print("Calling isfull")
    print(stk.isFull())
    stk.push(55)
    print(stk.stack)
    stk.push(10)
    stk.push(100)
    print("The removed value is ")
    print(stk.pop())
    stk.push(40)
    print(stk.stack)
    print(stk.isFull())




main()