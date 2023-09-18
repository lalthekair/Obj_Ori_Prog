"""
Classes and Objects
"""
# 12/9/2022
# for this exercise, we want to get the area of a circle


class Circle:
    # the area of a circle is pi * r^2, and pi is a constant
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return (self.radius ** 2) * 3.14

    def get_circumference(self):
        return (self.radius * 2) * 3.14


radius2 = Circle(3)
radius3 = Circle(5)


def main():
    print(radius2.get_area())
    print(radius2.get_circumference())


main()

# if you just did print(radius2) the output would be the memory address of the variable
print(radius2)
print(radius3)
print(radius2 == radius3)  # the output will be false because their memory addresses are different


"""Another Exercise"""
"""
Note: functions that are between the under-cases are dunder functions
the __init__ function is a dunder function
another dunder function is the __str__ function
"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # when you print the object/instance (by itself) after using this function you won't get the memory address
        return "This dog, aged " + str(self.age) + ", is called " + self.name + "."


dog1 = Dog("Cookie", 6)
dog2 = Dog("Rocky", 4)
print(dog1.name)
print(dog1)
print(dog2)  # observe the difference between earlier when we did print(radius2) and now

"""
NOTE:   __str__ function MUST return a value, as in you need to use the return keyword
        the values you return MUST be string, if it is an integer or a float then you need to convert it to string
"""

# the pass keyword


class Dogs:
    pass
    # by using pass you can have an empty class and run the code without python throwing an error


class Doggos:
    def __init__(self, breed):
        self.breed = breed

    def get_info(self):
        pass
        # you can also use it in functions
