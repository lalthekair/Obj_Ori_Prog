def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return f(n/2)
    else:
        return 1 + f(n**2 - 1)


def main():
    print(f(10))


main()