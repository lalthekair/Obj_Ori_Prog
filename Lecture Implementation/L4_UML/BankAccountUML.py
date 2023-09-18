class BankAccount:

    def __init__(self, account_id, name, bal):  # dunder method
        self.__id = account_id
        self.__name = name
        self.__balance = bal
        # The parameter names take from the third rectangle; the self. lines take from the second rectangle.
        # The init function is called implicitly without calling it when an object is instantiated.

    # Add the accessors to the code (getters/setters)
    # A good function only does ONE task.

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_id(self):  # Getters/Accessors (view the object attribute using a class method)
        return self.__id

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def set_name(self, modified_name):  # Setters/Mutators (change the object attribute using a class method)
        self.__name = modified_name

    # def __str__(self):
        # return "Customer ID:", self.__id, "\nCustomer name:", self.__name, "\nBalance:", self.__balance
