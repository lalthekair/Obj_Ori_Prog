class Calculator:

    def take_num1(self):
        n1 = float(input("Enter your first value: "))
        return n1

    def take_num2(self):
        n2 = float(input("Enter your second value: "))
        return n2

    def add(self, array1):
        total = 0
        for i in range(len(array1)):
            total += array1[i]
        return total

    def subtract(self, array2):
        difference = array2[0]
        for j in range(1, len(array2)):
            difference -= array2[j]
        return difference

    def multiply(self, array3):
        product = array3[0]
        for k in range(1, len(array3)):
            product *= array3[k]
        return product

    def divide(self):
        a = Calculator().take_num1()
        b = Calculator().take_num2()
        if b == 0:
            return "an error: division by zero is invalid."
        else:
            quotient = a / b
            return quotient

    def exponent(self):
        x = Calculator().take_num1()
        y = Calculator().take_num2()
        z = x ** y
        return z

    def find_remainder(self):
        p = Calculator().take_num1()
        q = Calculator().take_num2()
        if q == 0:
            return "an error: division by zero is invalid."
        else:
            remainder = p % q
            return remainder

