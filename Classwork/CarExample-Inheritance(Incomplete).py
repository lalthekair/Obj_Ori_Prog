from main import Automobile

class Car(Automobile):

    def __init__(self, make, year, mileage, price, doors):
        self.__doors = doors
        #super().__init__(make, year, mileage, price)
        Automobile.__init__(self, make, year, mileage, price)

    def get_doors(self):
        return self.__doors

    def set_doors(self, doors):
        if isinstance(doors, int):
            self.__doors = doors
        else:
            print("Invalid value")

    def __str__(self):
        return super().__str__() + "\nThe number of doors is " + str(self.__doors)
        #return Automobile.__str__(self) + "The number of doors is " + str(self.__doors)


def main():
    car1 = Car("Ford", 2020, 35.5, 3500.6,2)
    print(car1)
main()





class Automobile:

    def __init__(self, make, year, mileage, price):
        self.__make = make
        self.__year = year
        self.__mileage = mileage
        self.__price = price

    def get_make(self):
        return self.__make

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def set_make(self, make):
        if isinstance(make, str) == True:
            self.__make = make
        else:
            print("Invalid value")

    def set_year(self, year):
        if isinstance(year, int):
            self.__year = year
        else:
            print("Invalid value")

    def set_mileage(self, mileage):
        if isinstance(mileage, float):
            self.__mileage = mileage

    def set_price(self, price):
        if isinstance(price, float):
            self.__price = price

    def __str__(self):
        return "The make is " + self.__make + \
               "\nThe mileage is " + str(self.__mileage) +\
               "\nThe price is " + str(self.__price) +\
               "\nThe year is " + str(self.__year)