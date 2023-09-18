class Mammal:

    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print("I am a ", self.__species)

    def make_sound(self):
        print("All animals make sounds.")


class Dog(Mammal):

    """
    def __init__(self, species):
        super.__init__(species)
    """
    def __init__(self):
        super().__init__("Dog")

    def make_sound(self):
        print("Woof! Woof!")


class Cat(Mammal):

    """
    def __init__(self, species):
        super.__init__(species)
    """
    # do not need to re-initialize if i'm not adding new variables

    def make_sound(self):
        print("Meow")


def show_mammal_info(creature):
    if isinstance(creature, Mammal):
        creature.make_sound()
        creature.show_species()


def main():
    dog = Dog()
    mammal = Mammal('b')
    cat = Cat()

    '''
    dog.make_sound()
    dog.show_species()

    mammal.make_sound()
    mammal.show_species()

    cat.make_sound()
    cat.show_species()
    
    '''

    show_mammal_info(dog)
    show_mammal_info(mammal)
    show_mammal_info(cat)


main()