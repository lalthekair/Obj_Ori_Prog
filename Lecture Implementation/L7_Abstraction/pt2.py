""" MULTIPLE INHERITANCE """
# Write one class that implements 2 interfaces.

from abc import ABC, abstractmethod


class Interface1(ABC):
    @abstractmethod
    def method1(self):
        pass


class Interface2(ABC):
    @abstractmethod
    def method2(self):
        pass


class Implementation(Interface1, Interface2):
    def method1(self):
        print("This is from interface 1.")

    def method2(self):
        print("This is from interface 2.")
