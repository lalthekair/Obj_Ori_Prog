def fun(x):
    if x >= 10:
        return 3 * x + 5
    else:
        return fun(x + 2) - 3


def main():
    print("the result of fun(12) =  ", fun(12))


main()
