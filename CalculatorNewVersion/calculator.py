"""
The program asks the user to enter the operation. Then, the program takes some actions based on the selected
operation.
- Addition, Subtraction, and Multiplication:
    Asks the user about the numbers they need to  add/subtract/multiply.
    Then, takes the numbers and stores each in one index in an array.
    Finally, do the operation and return the result.
- Division, Remainder, and Exponent:
    Ask the user to enter two numbers, do the operation, and return the result.
"""
from supportiveMethods import Index


class Calculator(Index):

    def take_num1(self):
        n1 = float(input("Enter your first value: "))
        return n1

    def take_num2(self):
        n2 = float(input("Enter your second value: "))
        return n2

    def add(self, array1):
        total = 0
        for i in range(array1):
            total += array1[i]
        return total

    def subtract(self, array2):
        difference = 0
        for j in range(array2):
            difference -= array2[j]
        return difference

    def multiply(self, array3):
        product = 0
        for k in range(array3):
            product *= array3[k]
        return product

    def divide(self):
        a = self.take_num1()
        b = self.take_num2()
        if b == 0:
            return "Error: division by zero is invalid."
        else:
            quotient = a / b
            return quotient

    def exponent(self):
        x = self.take_num1()
        y = self.take_num2()
        z = x ** y
        return z

    def find_remainder(self):
        p = self.take_num1()
        q = self.take_num2()
        if q == 0:
            return "Error: division by zero is invalid."
        else:
            remainder = p % q
            return remainder

