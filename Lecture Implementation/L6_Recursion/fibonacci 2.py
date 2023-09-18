def main():
    print("The first 10 numbers in the modified Fibonacci series are: ")
    for number in range(0, 11):
        print(fib(number), end=", ")


def fib(n):
    """if n == 0 or n == 1 or n == 2:
        return 0"""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return fib(n-1) + fib(n-2) + fib(n-3) + fib(n-4)


main()