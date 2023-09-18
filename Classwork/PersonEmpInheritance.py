class Person:

    def __init__(self, n):
        self.__name = n

    def get_name(self):
        return self.__name

    def set_name(self, new_n):
        self.__name = new_n

    def __str__(self):
        return "The person's name is " + self.__name


class Employee(Person):

    def __init__(self,i, n):
        self.__id = i
        #super() is a built-in function in Python.
        # It creates an object from the parent class
        super().__init__(n)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def __str__(self):
        return super().__str__()+ "\nThe ID is " + str(self.__id)


def main():
    obj = Employee(123, "Ali")
    print(obj)
main()