class Automobile:

    def __init__(self, make, year, mileage, price):
        self.__make = make
        self.__year = year
        self.__mileage = mileage
        self.__price = price

    # isinstance(value, data type) methods are used for input validation

    def get_make(self):
        return self.__make

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def set_make(self, make):
        if not(isinstance(make, str)):
            print("Invalid input.")
        else:
            self.__make = make

    def set_year(self, year):
        if isinstance(year, int):
            self.__year = year
        else:
            print("Invalid input.")

    def set_mileage(self, mileage):
        if isinstance(mileage, float) is True:
            self.__mileage = mileage
        else:
            print("Invalid input.")

    def set_price(self, price):
        if isinstance(price, float):
            self.__price = price
        # else: print error is not part of the validation, adding it is optional

    def __str__(self):
        return "Make: " + self.__make + "\nModel: " \
               + str(self.__year) + "\nMileage: " + \
               str(self.__mileage) + "\nPrice: " + str(self.__price) + " SAR"

# encapsulation purpose is to decrease dependencies
# analyze  the code and state some improvements to it (inheritance, adding a parent class.)
# empty/incomplete code, complete UMl - complete code, empty/incomplete UML
# make sure to check the already written part too
# pay attention to the privacy settings of the instance attributes
