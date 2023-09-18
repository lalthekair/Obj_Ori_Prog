from coding import Car, ElectricCar, Petrolcar


def call_funcs_poly(obj):
    if isinstance(obj, Car):
        print(obj.drive())


def main():
    elec = ElectricCar(100)
    petrol = Petrolcar(800)
    print("What kind of car do you drive?\n1. Electric\n2. Petrol")
    user = int(input("> "))
    if user == 1:
        call_funcs_poly(elec)
    elif user == 2:
        call_funcs_poly(petrol)


main()