from bank_account import BankAccount


# This file contains the main functions
def main():
    user1 = BankAccount(10)
    print("Here I will call the accessor method: ")
    print(user1.get_balance())


"""
    user1= BankAccount(10)
    print("The balance is: ", user1.__balance)
    user1.deposit()
    print("The balance is: ",user1.__balance)

    user1.withdraw()
    print("The balance is ",user1.__balance)

    print("Updating the balance: ",user1.__balance)
    user1.__balance=1000

    print("The new balance is ",user1.__balance)
"""


main()
