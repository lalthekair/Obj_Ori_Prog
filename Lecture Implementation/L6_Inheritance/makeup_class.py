class Car:

    def __init__(self, mk, md, y):
        self.__make = mk
        self.__model = md
        self.__year = y

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def set_make(self, new_mk):
        if isinstance(new_mk, str):
            result = new_mk.strip()  # removes all the empty spaces
            if result != "":  # second layer of validation
                self.__make = result

    def set_model(self, new_md):
        if isinstance(new_md, str):
            result = new_md.strip()
            if result != "":
                self.__model = result

    def set_year(self, new_y):
        if isinstance(new_y, int) and new_y >= 1800:
            self.__year = new_y

    def __str__(self):
        result = "Make: " + self.__make
        result += "\nModel: " + self.__model
        result += "\nYear: " + str(self.__year)
        return result


def main():
    cars_lst = [Car("Toyota", "RAV4", "2022"), Car("Ford", "Explorer", 2016), Car("Kia", "Carnival", 2021),
                Car("Mazda", "CX-5", 2019), Car("Porsche", "Cayenne", 2023)]
    # Iterate over the list of cars and perform the following for each car:
    # 1) Set the year of the car to 2020
    # 2) Print a full summary about the car
    for x in cars_lst:
        x.set_year(2020)
        print(x)


main()
