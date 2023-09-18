from modules.library_item import LibraryItem


class Book(LibraryItem):

    def __init__(self, title, upc, genre, isbn, authors):
        self.__isbn = isbn
        self.__authors = authors
        super().__init__(title, upc, genre)

    def get_isbn(self):
        return self.__isbn

    def get_authors(self):
        return self.__authors

    def set_authors(self, authors):
        self.__authors = authors

    def find_author(self, author):
        """if author in self.__authors:
            return self.__authors.index(author)
        else:
            return "Author not found." """
        pass

    def modify_author(self, index, new_name):
        # self.__authors[index] = new_name
        pass

    def __str__(self):
        return super().__str__() + '\nISBN: ' + str(self.__isbn) + '\nAuthors: ' + str(self.__authors)
