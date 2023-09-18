"""
1) Write 1 class of your own. The class must meet the following requirements:
- A minimum of 2 attributes
- A minimum of 2 functions
- A __str__ method that formats and displays the object’s attributes

2) Add all necessary commands to print the values in your program.
"""


class Laptop:
    def __init__(self, brand, memory, storage):
        self.brand = brand
        self.memory = memory
        self.storage = storage

    def __str__(self):
        return "The " + self.brand + " laptop has " + str(self.memory) + " GB of RAM memory and " + \
               str(self.storage) + " GB of SSD storage."

    def recommendation(self):
        print("\nThe", self.brand, "laptop:")
        if self.memory <= 4 or self.storage <= 216:
            print("This laptop is not recommended for programmers.")
        else:
            print("This laptop is okay for programmers.")


pc1 = Laptop("Lenovo", 16, 1024)
pc2 = Laptop("Dell", 8, 512)
pc3 = Laptop("Asus", 4, 128)

print(pc1)
print(pc3)
pc2.recommendation()
