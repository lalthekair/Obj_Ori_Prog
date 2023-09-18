class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        return "Car"


class ElectricCar(Car):
    def __init__(self, make, model, batteryLevel):
        self.batteryLevel = batteryLevel
        super().__init__(make, model)

    def drive(self):
        return "Electric Car"


class PetrolCar(Car):
    def __init__(self, make, model, fuelLevel):
        self.fuelLevel = fuelLevel
        super().__init__(make, model)

    def drive(self):
        return "Petrol Car"



def call_functions(x):
    if isinstance(x, Car):
        return x.drive()
    else:
        return "Invalid Object"


def main():
    ec = ElectricCar(2022, "RAV4", 35)
    pc = PetrolCar(2016, "Explorer", 438)
    print(call_functions(ec))
    print(call_functions(pc))


main()