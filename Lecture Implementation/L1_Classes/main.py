# Lab Exercise 1
# Class no.1 - Cats

class Cats:
    def __init__(self, breed, color, name):
        self.breed = breed
        self.color = color
        self.name = name

    def get_data(self):
        print(self.name, "is a", self.color, self.breed)


cat1 = Cats("Siamese", "White and Brown", "Gloria")
cat2 = Cats("British Shorthair", "Grey", "Cinderella")
cat3 = Cats("Bengal", "Zebra Brown", "Maui")
cat1.get_data()
cat2.get_data()
cat3.get_data()
print(cat2.color, "is a cute color for a", cat2.breed)
print(cat3.name, "is much naughtier than", cat1.name)
print("")

##########################################################################


# Class no.2 - Inventory
class Inventory:
    def __init__(self, item, qty, unit_price, supplier):
        self.item = item
        self.qty = qty
        self.unit_price = unit_price
        self.supplier = supplier

    def get_inv(self):
        print(self.item, ":", self.qty, "remaining.")
        if self.qty > 4:
            print("Inventory sufficient.")
        else:
            print("More inventory is needed; reach out to", self.supplier, "\nUnit price:", self.unit_price)


broom = Inventory("Handheld broom", 3, 15.99, "Extra")
chair = Inventory("Spinning chair", 14, 49.99, "Hamza Baroum Inc.")
notepad = Inventory("Notepad", 20, 5.75, "Amazon SA")
broom.get_inv()
chair.get_inv()
notepad.get_inv()
print(notepad.qty, notepad.item, 'is a large number of items to have!')
print("Why do we even have a", broom.item, "in our warehouse?")
print("I like", chair.item, "but why do we have", chair.qty, "of them?")
