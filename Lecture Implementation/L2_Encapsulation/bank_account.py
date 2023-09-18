class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self):
        amount = float(input("Enter the amount: "))
        self.__balance = self.__balance + amount
        return self.__balance

    def withdraw(self):
        amount = float(input("Enter withdrawal amount:"))
        self.__balance = self.__balance - amount
        return self.__balance

    def get_balance(self):  # getter or accessor
        return self.__balance
