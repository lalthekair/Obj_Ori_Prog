class BankAccounts:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        x = float(input("Enter deposit amount: "))
        self.balance += x
        print("Current balance: ", self.balance)

    def withdraw(self):
        y = float(input("Enter withdraw amount: "))  # float is better because you might deposit/withdraw fractions
        self.balance -= y
        print("Current balance: ", self.balance)

    def get_bal(self):
        print("Your current balance is", self.balance)
