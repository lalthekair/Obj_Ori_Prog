"""
Exceptions are errors that arise and causes the program to crash during the running time.

Types of exceptions:
1- Syntax Error - in the code itself
2- Logical Error - in the logic of the program
3- Runtime Error (type, index, value) - causes the program to crash
"""


class Division:

    def divide(self):

        try:
            num1 = int(input("Enter first value: "))
            num2 = int(input("Enter second value: "))
            result = num1/num2
            print(result)
        except ValueError:
            print("I've caught an exception.")
        except ZeroDivisionError:  # This exception handles zero errors only
            # try and catch an exception
            print("I've caught a zero division exception.")
        except KeyboardInterrupt:
            print("The user stopped the program.")
        else:
            print("No exception raised")
        finally:  # this code runs regardless if an exception raised or not
            print("We're done.")


def main():
    d = Division()
    d.divide()


main()