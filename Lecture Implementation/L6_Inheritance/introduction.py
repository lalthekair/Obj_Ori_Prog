# Slide 14

class Person:
    def __init__(self, n):
        self.__name = n

    # getter/accessor; access the data of the private attribute from outside the class
    def get_name(self):
        return self.__name
        # always has a return

    # setter/mutator; change or update the value of the private attribute from outside the class
    def set_name(self, new_n):
        self.__name = new_n
        # does not have a return

    def __str__(self):
        return "Name: " + self.__name


class Employee(Person):  # class Child(Parent)
    def __init__(self, i, n):  # We declare the parameters as normal
        self.__id = i
        super().__init__(n)  # We tie the parameter with the instance attribute from the parent

        # "go to the init in the parent and take everything from there"
        # super() is a built-in function that "opens the door" for the child class to the parent

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def __str__(self):
        # cannot do return "Name:" + self.__name + "\nID:" + self.__id because encapsulation
        return super().__str__() + "\nID :" + str(self.__id)
        # super().functionName
        # possible errors: cannot concatenate str and int, cannot access Employee.__name (must use super)


def main():
    obj = Employee(101, "Omar")
    print(obj)
    print(obj.get_name())


main()
