from modules.disc import Disc


class DVD(Disc):

    def __init__(self, title, upc, genre, yr, prod, actors, dir):
        self.__actors = actors
        self.__director = dir
        super().__init__(title, upc, genre, yr, prod)

    def get_actors(self):
        return self.__actors

    def get_director(self):
        return self.__director

    def set_actors(self, actors):
        self.__actors = actors

    def set_director(self, d):
        self.__director = d
        
    def __str__(self):
        return super.__str__(self) + '\nYear: ' + str(self.get_year()) + '\nProducer: ' + self.get_producer() + \
               '\nActors:' + self.__actors + '\nDirector: ' + self.__director