from modules.library_item import LibraryItem


class Magazine(LibraryItem):

    def __init__(self, title, upc, genre, vol, issue):
        self.__volume = vol
        self.__issue = issue
        super().__init__(title, upc, genre)

    def get_volume(self):
        return self.__volume

    def get_issue(self):
        return self.__issue

    def set_volume(self, v):
        self.__volume = v

    def set_issue(self, i):
        self.__issue = i

    def __str__(self):
        return super().__str__() + '\nVolume: ' + str(self.__volume) + '\nIssue: ' + str(self.__issue)
    