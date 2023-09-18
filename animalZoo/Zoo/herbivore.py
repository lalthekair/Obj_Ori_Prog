from Zoo.zooAnimal import ZooAnimal


class Herbivore(ZooAnimal):

    def __init__(self, yr_born, yr_brought):
        super().__init__(yr_born, yr_brought)

    def eat(self):
        print("Herbivore eats plants")
