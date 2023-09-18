"""
Recursion is basically a loop. Loop and recursion are both fundamentally repetition sequences.
If there is no reason to stop the recursion from repeating, it will keep going; see name_printing() function.
We need to add a way to atop it.

Recursion:
1- base step
2- recursive step
"""
# Create a function that uses recursion to print a name 5 times


def print_name(x):
    print("Hello")
    x -= 1
    if x != 0:
        print_name(x)


    # better code:
def better_print_name(y):
    if y == 0:
        quit()  # built-n function that will enable the program to exit the block it is in
    print("Hey")
    better_print_name(y-1)


def name_printing():
    print("Hi")
    name_printing()


def main():
    better_print_name(5)


main()
