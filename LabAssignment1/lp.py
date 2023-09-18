class Laptop:

    def __init__(self, s, m, y, p, size):
        self.__serial_number = s
        self.__manufacturer = m
        self.__year_manufactured = y
        self.__price = p
        self.__screen_size = size
        # the variables with the init function are the ones next to self

    def get_serial_number(self):
        return self.__serial_number

    def get_manufacturer(self):
        return self.__manufacturer

    def get_year_manufactured(self):
        return self.__year_manufactured

    def get_price(self):
        return self.__price

    def get_screen_size(self):
        return self.__screen_size

    def set_year_manufactured(self, new_y):
        self.__year_manufactured = new_y

    def set_price(self, new_p):
        self.__price = new_p

    def set_screen_size(self, new_size):
        self.__screen_size = new_size

    def __str__(self):
        return "Serial Number: " + str(self.__serial_number) + "\nManufaturer: " + self.__manufacturer + "\nYear: " + \
               str(self.__year_manufactured) + "\nPrice: " + str(self.__price) + " SAR\nScreen Size: " + \
               str(self.__screen_size) + " in."
