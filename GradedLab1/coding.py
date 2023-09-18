from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def drive(self):
        pass


class ElectricCar(Car):
    def __init__(self, batteryLevel):
        self.__batteryLevel = batteryLevel

    def drive(self):
        return "Hello from Electric Car class"

    def charge(self):
        pass


class Petrolcar(Car):
    def __init__(self, fuelLevel):
        self.__fuelLevel = fuelLevel

    def drive(self):
        return "Hello from Petrol Car class"

    def fullUp(self):
        pass