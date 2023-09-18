from BankAccountUML import BankAccount

obj = BankAccount(101, "Abeer", 35.45)

# Use the appropriate functions to view the balance, deposit x, and view it again.
# Then, view the name, change it to y, and check it again.
print(obj.get_balance())
obj.deposit(int(input("Enter the deposit amount: ")))
print(obj.get_balance())

print(obj.get_name())
obj.set_name(input("Enter new name: "))
print(obj.get_name())
