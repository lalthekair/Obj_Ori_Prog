from Try1 import Stack


def main():
    stk = Stack(5)
    print(stk.isEmpty())
    print("I will push 5.")
    stk.push(5)
    print(stk.isEmpty())
    print("Calling Stack.isFull() ... ")
    print(stk.isFull())
    stk.push(46)
    print(stk.get_stack())
    stk.push(10)
    stk.push(300)
    stk.push(5)
    print(stk.get_stack()) #!
    print("Calling Stack.isFull() ... ")
    print(stk.isFull())
    stk.pop()
    stk.pop()
    print(stk.get_stack())


main()
