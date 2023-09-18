class Car:

    def __init__(self, mk, md, y):
        self.__make = mk
        self.__model = md
        self.__year = y

    def get_year(self):
        return self.__year

    def get_model(self):
        return self.__model

    def get_make(self):
        return self.__make

    def set_year(self, new_y):
        if isinstance(new_y, int) == True:
            if new_y > 0:
                self.__year = new_y
        else:
            print(new_y, " is an invalid value")

    def set_make(self, new_mk):
        if isinstance(new_mk, str) == True:
            result = new_mk.strip()
            if result != "":
                self.__make = result
            else:
                print("You didn't enter a real value")
        else:
            print(new_mk, " is not a string value")

    def set_model(self, new_md):
        if isinstance(new_md, str) == True:
            result = new_md.strip()
            if result != "":
                self.__model = result
            else:
                print("You didn't enter a real value")
        else:
            print(new_md, " is not a string value")

    def __str__(self):
        result = "The car is manufactured by " + self.__make
        result+= "\nThe model is " + self.__model
        result+= "\nThe year is " + str(self.__year)

        return result


def main():
    car1 = Car("Ford", "Torus", 2020)
    print(car1)


main()