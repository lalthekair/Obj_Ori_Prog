class Book:

    def __init__(self, t, a, y, n):
        self.__title = t
        self.__author = a
        self.__published_year = y
        self.__number_of_pages = n

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_published_year(self):
        return self.__published_year

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_published_year(self, new_y):
        self.__published_year = new_y

    def set_number_of_pages(self, new_n):
        self.__number_of_pages = new_n

    def __str__(self):
        return "Title: " + self.__title + "\nAuthor: " + self.__author + "\nYear: " + str(self.__published_year) + \
            "\nNo. of Pages: " + str(self.__number_of_pages)
