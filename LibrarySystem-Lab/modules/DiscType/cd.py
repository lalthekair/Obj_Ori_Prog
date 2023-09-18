from modules.disc import Disc
from modules.library_item import LibraryItem


class CD(Disc):

    def __init__(self, title, upc, genre, yr, prod, art):
        self.__artist = art
        super().__init__(title, upc, genre, yr, prod)

    def get_artist(self):
        return self.__artist

    def set_artist(self, a):
        self.__artist = a

    def __str__(self):
        return LibraryItem.__str__(self) + '\nYear: ' + str(self.get_year()) + '\nProducer: ' + self.get_producer() + \
               '\nArtist :' + self.__artist
