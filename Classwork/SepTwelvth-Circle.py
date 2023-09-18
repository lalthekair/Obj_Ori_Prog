#Lab Exercise:
#Create a class called Circle
#The class has 1 instance attribute, radius
#The class has 1 instance method, calculate_area(). This method prints the area of the circle
#Instantiate an object from class Circle. The radius is 3
#Call the function calculate_area() and observe your output.

#Note: Area = pi * r^2, pi = 3.14

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        res = 3.14 * self.radius * self.radius
        print(res)

c1 = Circle(3)
c1.calculate_area()