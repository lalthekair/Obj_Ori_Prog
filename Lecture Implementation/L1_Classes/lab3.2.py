"""
Exercise 2: calculator class
"""


class Calculator:
    def __init__(self):
        pass

    def addition(self):
        a = int(input("Enter amount 1: "))
        b = int(input("Enter amount 2: "))
        print(float(a+b))

    def subtraction(self):
        c = int(input("Enter amount 1: "))
        d = int(input("Enter amount 2: "))
        print("amount 2 - amount 1 is:", float(d-c))

    def multiplication(self):
        x = int(input("Enter amount 1: "))
        y = int(input("Enter amount 2: "))
        print(float(x*y))


User1 = Calculator()


def main():
    User1.addition()
    User1.subtraction()
    User1.multiplication()


main()
