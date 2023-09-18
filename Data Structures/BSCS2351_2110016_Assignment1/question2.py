def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return f(n/2)
    else:
        return 1 + f(n**2 - 1)


def main():
    print("f(0) is", f(0))
    print("f(10) is", f(10))
    print("f(5) is", f(5))


main()