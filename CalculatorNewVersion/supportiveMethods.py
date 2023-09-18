from calculator import Calculator


class Index:

    def add_to_arr(self):
        elements = int(input("Enter number of values: "))
        array4 = []
        for s in range(elements):
            num = float(input("Enter value: "))
            array4.append(num)
        return array4

    def determine_operation(self, selected_operation):
        print("You have selected " + selected_operation)

        if selected_operation == "+":
            addition = self.add_to_arr()
            output = Calculator.add(self, addition)

        elif selected_operation == "-":
            output = Calculator.subtract(self, self.add_to_arr())

        elif selected_operation == "*":
            output = Calculator.multiply(self, self.add_to_arr())

        elif selected_operation == "%":
            output = Calculator.find_remainder(self)

        elif selected_operation == "/":
            output = Calculator.divide(self)

        elif selected_operation == "^":
            output = Calculator.exponent(self)

        else:
            print("You must enter a valid operation!")
            return

        print("The result is ", output)
