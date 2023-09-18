from children import Car
from children import Truck
from children import SUV
# Import all the derived/subclasses because that is what we're instantiating from.


def main():
    car1 = Car("Ford", 2020, 16.8, 55000, 4)
    truck1 = Truck("Mercedes", 2015, 30.1, 70000, "AWD")
    SUV1 = SUV("Toyota", 2022, 23.4, 15000, 5)
    print(car1)
    print()
    print(truck1)
    print()
    print(SUV1)
    print("\n")
    print(car1.get_make())


main()
