from parent import Automobile


class Car(Automobile):

    def __init__(self, make, year, mileage, price, doors):
        # super().__init__(make, year, mileage, price)
        Automobile.__init__(self, make, year, mileage, price)
        self.__doors = doors

    def get_doors(self):
        return self.__doors

    def set_doors(self, doors):
        if isinstance(doors, int):
            self.__doors = doors
        else:
            print("Invalid value.")

    def __str__(self):
        return Automobile.__str__(self) + "\nDoors: " + str(self.__doors)
        # super().__str__()


class Truck(Automobile):

    def __init__(self, make, year, mileage, price, drive_type):
        Automobile.__init__(self, make, year, mileage, price)
        self.__drive_type = drive_type

    def get_doors(self):
        return self.__drive_type

    def set_doors(self, drive_type):
        if isinstance(drive_type, str):
            self.__drive_type = drive_type
        else:
            print("Invalid value.")

    def __str__(self):
        return super().__str__() + "\nDrive Type: " + self.__drive_type


class SUV(Automobile):
    def __init__(self, make, year, mileage, price, pass_cap):
        # super().__init__(make, year, mileage, price)
        Automobile.__init__(self, make, year, mileage, price)
        self.__pass_cap = pass_cap

    def get_doors(self):
        return self.__pass_cap

    def set_doors(self, pass_cap):
        if isinstance(pass_cap, int):
            self.__pass_cap = pass_cap
        else:
            print("Invalid value.")

    def __str__(self):
        return super().__str__() + "\nPassenger Capacity:" + str(self.__pass_cap)
