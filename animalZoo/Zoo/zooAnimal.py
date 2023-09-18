class ZooAnimal:
    def __init__(self, yr_born, yr_brought):
        self.__year_born = yr_born
        self.year_brought_to_zoo = yr_brought



    def get_year_brought_to_zoo(self):
        return self.year_brought_to_zoo

    def calculate_age_when_brought_to_zoo(self):
        return self.year_brought_to_zoo

    def eat(self):
        print("Animals eat what their bodies need")


z = ZooAnimal(1991,2018)
print(z.__year_born)