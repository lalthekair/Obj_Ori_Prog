def summation(x):
    if x == 0:
        return 0  # base step
    else:
        return summation(x-1) + x  # recursive step


def main():
    """while True:
        user = input("Enter value: ")
        if isinstance(user, int):
            print("The summation of (", int(user), ") =  ", summation(int(user)))
            break
        else:
            print("Invalid value.")
            continue"""
    user = int(input("Enter value: "))
    print("The summation of (", user, ") =", summation(user))


main()
