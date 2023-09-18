from BankAccounts import BankAccounts
# syntax: from filename import class_name


def main():
    user1 = BankAccounts(20)
    user1.deposit()
    user1.withdraw()
    user1.get_bal()


main()
