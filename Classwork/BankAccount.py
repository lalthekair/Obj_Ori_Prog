class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter the amount"))
        self.balance = self.balance + amount
        #self.balance +=amount
        print(self.balance)

    def withdraw(self):
        amount = float(input("Enter withdrawal amount"))
        self.balance = self.balance - amount
        return self.balance


