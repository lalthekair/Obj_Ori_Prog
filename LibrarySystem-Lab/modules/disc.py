from modules.library_item import LibraryItem


class Disc(LibraryItem):

    def __init__(self, title, upc, genre, yr, prod):
        self.__year = yr
        self.__producer = prod
        super().__init__(title, upc, genre)

    def get_year(self):
        return self.__year

    def get_producer(self):
        return self.__producer

    def set_year(self, y):
        self.__year = y

    def set_producer(self, p):
        self.__producer = p
