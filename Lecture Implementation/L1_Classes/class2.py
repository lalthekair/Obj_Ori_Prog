# Create a class called Dog
class Dog:

    # The class has five instance (object) attributes which are ...
    # the init function is the constructor in python
    def __init__(self, name, age, color, breed, owner):  # Between () - parameters.
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.owner = owner  # All these are instance attributes. The only way to use them is with an object.
        # We are giving an initial value to the instance attributes.
        # The constructor gives initial values to the attributes, which are then the formulas for objects to fit into.

    # In the class, write an instance function (a function that works only with objects) named "Find Owner"
    # that prints information about the dog and its owner.
    def get_data(self):  # self is automatically added because it is an instance function.
        # print(self.name, 'is the best furry friend of', self.owner)
        print('The dog\'s name is', self.name, 'and its owner is', self.owner, ".",
              self.name, "is a", self.color, self.breed, "who is", self.age, "years old.")

    def __str__(self):
        string = self.name + ' is the best furry friend of ' + self.owner
        return string


# Inside the class is the program; inside the object is the actual data - remember the Word analogy.
# Instantiate three objects from class Dog.
# Create three objects from class Dog.
dog1 = Dog("Cookie", 6, "Light Brown", "Pug", "Rosanna")
dog2 = Dog("Dalgom", 5, "White", "Shih Poo", "Jisoo")
dog3 = Dog("Hank", 2, "White and Brown", "Mixed", "Chaeyeong")
# Objects should be created outside the class.

# Do the necessary calls to print *Dalgom* in the output.
print(dog2.name)

"""
Write the necessary commands to get the following output:
(Include all the necessary calls - aka use the function and not print string.)
Cookie
Dalgom
Hank
Chaeyeong is the owner of Hank
"""
print(dog1.name)
print(dog2.name)
print(dog3.name)
print(dog3.owner, "is the owner of", dog3.name)

"""
IN REFERENCE TO THE CLASS ABOVE; CODE:
dogx = Dog("Mike", "Golden", 2, "Retriever", "Jack")
print(dogx.age, dogx.color)
Analyze the code and write the output.

(Color and age are switched in the object code, so the output will be "Golden 2".)
"""

# Use the get_data function to get information about dog 2. Syntax: object.class()
print("")
dog2.get_data()  # Put the arguments you want to pass in the parameters *if* the function accepts parameters.
print(dog1)
