from supportiveMethods import Index


def main():
    repeat = True
    while repeat:
        print("Select one of the following operations: \n+ \n- \n* \n/ \n%\n^\n")
        op = input()
        while op != '+' and "-" and '*' and '/' and '%' and '^' and '"':
            print("Invalid request! Please select a valid operation.")
        Index.determine_operation(op)
        user = input("Would you like to perform another operation? Y/N ")
        if user == 'Y':
            repeat = True
        elif user == 'N':
            repeat = False


main()
