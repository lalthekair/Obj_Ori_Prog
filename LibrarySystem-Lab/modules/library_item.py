class LibraryItem:

    def __init__(self, title, upc, genre):
        self.__title = title
        self.__upc = upc
        self.__genre = genre
        self.__inStock = True

    def get_title(self):
        return self.__title

    def get_upc(self):
        return self.__upc

    def get_genre(self):
        return self.__genre

    def set_title(self, t):
        self.__title = t

    def set_genre(self, g):
        self.__genre = g

    def borrow_item(self):
        pass

    def return_item(self):
        pass

    def __str__(self):
        t1 = "Title: " + self.__title
        upc1 = "UPC: " + str(self.__upc)
        g1 = "Genre: " + self.__genre
        a1 = "Available: " + str(self.__inStock)
        return t1 + '\n' + upc1 + '\n' + g1 + '\n' + a1
