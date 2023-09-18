from StackImplementation import Stack


def main():
    stk = Stack()
    name = input("Enter the name ")

    for i in range(len(name)):
        stk.push(name[i])

    reveredString = ""
    for i in range(len(name)):
        reveredString += stk.pop()

    print("The reversed string of ", name, ' is ', reveredString)


main()
