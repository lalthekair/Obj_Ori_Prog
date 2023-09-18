from Try1 import Stack


def main():
    stk = Stack(5)  # initiating an object
    name = input("Enter the name ")

    i = 0  # starting the counter to push the letters one by one in the stack
    while i < len(name):  # we're starting from the ground up
        stk.push(name[i])  # push the letter with the index i into the stack
        i += 1  # increase the counter by 1

    reveredString = ""  # empty string to begin appending the letters to
    while stk.len() != 0:  # as long as the stack still has stuff in it and is not empty
        reveredString += stk.pop()  # add the popped letter to the string

    print("The reversed string of ", name, ' is ', reveredString)


main()
