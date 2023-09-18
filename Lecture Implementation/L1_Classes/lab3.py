"""
Exercise 1: instantiate a class for a user's bank account.
"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, x):
        print("\n\tAmount deposited:", x)
        self.balance += x
        print("\n\tAvailable balance =", self.balance)

    def withdraw(self, y):
        print("\n\tYou withdrew: ", y)
        self.balance -= y
        print("\n\tAvailable balance =", self.balance)

    def display(self):
        print("Your current balance is", self.balance)


User1 = BankAccount(10.00)


def main():
    print("Hello! Welcome to the Deposit and Withdrawal Machine")
    User1.display()
    deposit_amount = float(input("Enter amount to be deposited: "))
    User1.deposit(deposit_amount)
    withdraw_amount = float(input("Enter the amount to be withdrawn: "))
    User1.withdraw(withdraw_amount)


main()
