def main():
    print("The first 10 numbers in the Fibonacci series are: ")
    for number in range(0, 11):
        print(fib(number), end=", ")


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


main()