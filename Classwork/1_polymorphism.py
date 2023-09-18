class Mammal:
    
    def __init__(self, species):
        self.species = species
        print("Parent class")
        
    def show_species(self):
        print("I am a ", self.species)
        
    def make_sound(self):
        print("All animals make sound")


class Dog(Mammal):
    
    def __init__(self, species, name):
        self.name = name
        print("Child class")
        super().__init__(species)
        
    def make_sound(self):
        print("Woof Woof. Dogs are barking")
        


class Cat(Mammal):

    def show_owner(self):
        print("The cat owner is Joud.")

    def make_sound(self):
        print("Meow")


def get_func(obj):
    # usually, syntax to call class method is objectName.method_name()
    obj.make_sound()
    # second class method
    # third class method
    # ...
    # this decreases complication and increases simplicity by reducing code lines and calling methods repeatedly
    # once function that calls all the methods for various classes as long as there is inheritance between them


def main():

    cat = Cat("cat")
    cat.show_owner()
    cat.show_species()
    print("Which make_sound() will be called?")
    get_func(cat)  # instead of cat.make_sound()

    child = Dog("A", "D")
    child.show_species()
    print("Which make_sound() will be called?")
    child.make_sound()
    
    print("Which make_sound() will be called?")
    parent = Mammal("A")
    parent.make_sound()


main()