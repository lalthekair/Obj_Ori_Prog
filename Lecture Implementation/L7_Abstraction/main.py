"""
1) An interface has at least one or more abstract methods
2) Abstract methods are defined in the INTERFACE and have no implementation
3) All abstract methods must be implemented in the implementation class
4) Objects cannot be instantiated from the interface class because they are special types of classes

- implementation parameters follow what has been defined in the interface
- python will throw an error if not all abstract methods were implemented
- ABC = Abstract Base Classes
- each word carries a mark; ALL DETAILS are extremely important
- both classes, the interface and implementation, will have inheritance

An interface is just the outside view that the end-user deals with, which divides from the code and covers
the underlying implementation.
"""

from abc import ABC, abstractmethod



class InterfaceCar(ABC):  # syntax; class Name(ABC): to inherit all the features of an interface

    """def pushGas(self):
        pass"""
    # this is an instance method (can be called n times) NOT abstract
    # static method is created inside the class and has one form (does not use any instance attributes)

    @abstractmethod
    def push_gas(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def brake(self, type):  # type is a parameter, not an instance attribute
        pass
    # identifying the error would be in the syntax as well as rules/conventions



class ImplementationCar(InterfaceCar):  # ABC is the grandpa

    def push_gas(self):
        print("Car is accelerating.")

    def start_engine(self):
        print("Engine starting ...")

    def brake(self, type):
        if type == 1:
            print("Car is decelerating.")
        elif type == 2:
            print("Handbrake engaged.")



def main():
    # create object; I should know which class to create the object from
    car1 = ImplementationCar()
    # possible errors:
    # creating object from interface class, not importing requirements, not implementing all abstract methods

    # call methods
    car1.start_engine()
    car1.push_gas()
    car1.brake(1)



main()