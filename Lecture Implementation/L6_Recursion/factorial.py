def fact(x):
    if x == 1:
        return 1  # base step
    else:
        return fact(x-1) * x  # recursive step


def main():
    print("The factorial of (4) =  ", fact(4))


main()
