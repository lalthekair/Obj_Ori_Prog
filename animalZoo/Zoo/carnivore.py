from Zoo.zooAnimal import ZooAnimal


class Carnivore(ZooAnimal):

    def __init__(self, yr_born, yr_brought):
        super().__init__(yr_born, yr_brought)

    def eat(self):
        print("Carnivore eats meat")
