"""
BSCS 2355 – Assignment 1

Monday, October 17, 2022
Leena Althekair
2110016
"""

from supportiveMethods import Index


def main():
    repeat = True
    while repeat:
        print("Select one of the following operations: \n+ \n- \n* \n/ \n%\n^")
        op = input()
        if op != '+' and op != "-" and op != '*' and op != '/' and op != '%' and op != '^':
            print("Invalid request! Please select a valid operation.")
            continue

        Index().determine_operation(op)
        invalid = True
        while invalid:
            user = input("Would you like to perform another operation? Y/N ")
            if user == 'Y':
                repeat = True
                invalid = False
            elif user == 'N':
                repeat = False
                invalid = False
                print("Thank you! Exiting the program ...")
            else:
                invalid = True
                print("Invalid request.")


main()
