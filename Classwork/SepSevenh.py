#Create a class called Dog
class Dog:
    
    #The class has 5 instance atributes
    def __init__(self, name, age, color, breed, owner):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed
        self.owner = owner
    #write an instance function named find_owner that prints information about the dog and its owner
    def find_owner(self):
        print("The dog's name is ", self.name , " and its owner is ", self.owner)

#instantiate 3 objects from class Dog
#Create 3 objects from class Dog
dog1 = Dog("Arthur", 1, "Golden", "Huskie", "Nour")
dog2 = Dog("Ema", 2, "Brown", "Huskie", "Nanny")
dog3 = Dog("Lio", 1.5, "Brown", "Huskie", "Harry")

#Do the necessary calls to print Arthur in the output
print(dog1.name)
        
        
#Do all necessary commands to get the output as shown
print(dog2.name)
print(dog3.name)
print(dog3.owner, " is the owner of ", dog3.name)

#use find_owner to print information about dog1
dog1.find_owner()



        
        
        
        
        
        
        