def add_even_integers_only(lst, num):
    if isinstance(num, int) is False:
        raise TypeError("This is not an integer.")
    elif num % 2 == 1:
        raise ValueError("This is not an even number.")
    else:
        lst.append(num)
        print(lst)


def main():
    """lst = []
    while True:
        add_even_integers_only(lst, 4)  # cannot pass an input because it will always be entered as a string
        print(lst)
        if input("Would you like to add another value? y/n _") != 'y':
            break"""
    lst = [10, 20]
    add_even_integers_only(lst, 12)  # "F", 50'


main()