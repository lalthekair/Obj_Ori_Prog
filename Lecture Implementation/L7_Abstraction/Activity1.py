"""
Create an interface called Shape. This interface has one abstract method, calculate_area()

- Write a class, named Rectangle, that implements the above interface. This class calculates the area of the Rectangle
and returns the result, noting that area = width * height.
- Write a class, named Circle, that also implements the Shape interface. This class calculates the area of the circle
and returns the result, noting that area = 3.14 * r^2
- In main():
    - instantiate an object and name it shape1
    - print the area of shape1
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self, n1, n2):
        pass


class Rectangle(Shape):
    def calculate_area(self, n1, n2):
        area = n1 * n2
        return area


class Circle(Shape):
    # To avoid the requirement of passing two arguments to the implementation method, there are two ways:
    #   1- Ask the user to input the data within the class method itself instead of passing it as an argument.
    #   2- Initialize the variables in the dunder function of the child class.
    # Both of these methods would mean that the abstract method will have no parameters.
    def calculate_area(self, n1, n2=None):
        area = n1 ** 2 * 3.14
        return area


def main():
    shape1 = Circle()
    print(shape1.calculate_area(4))


main()