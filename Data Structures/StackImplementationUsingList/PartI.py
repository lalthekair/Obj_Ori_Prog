from StackImplementation import Stack


def main():
    stk = Stack()
    name = input("Enter the name ")

    i = len(name) * 2
    j = 0
    while i > len(name):
        stk.push(name[j])
        i -= 1  # number of times the loop will run
        j += 1  # the index of the name

    reveredString = ""
    while stk.isEmpty() is False:  # is can be used instead of == in this scenario
        reveredString += stk.pop()

    print("The reversed string of", name, 'is', reveredString)


main()
