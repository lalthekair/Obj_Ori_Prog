class BankAccount:

    def __init__(self, account_id, name, bal):
        self.__id = account_id
        self.__name = name
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def set_name(self, modified_name):
        self.__name = modified_name


obj = BankAccount(111,"Abrar", 3.5)
print(obj.get_balance())
obj.deposit(5)
print(obj.get_balance())

print(obj.get_name())
obj.set_name("Haya")
print(obj.get_name())