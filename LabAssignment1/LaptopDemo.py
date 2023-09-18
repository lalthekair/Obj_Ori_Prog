from lp import Laptop


def main():
    hp = Laptop(101, "HP", 2012, 4599, 15)
    macbookPro = Laptop(102, "Apple", 2020, 7899, 15)
    macbookAir = Laptop(103, "Apple", 2020, 5299, 13)
    asus = Laptop(104, "ASUS", 2021, 7899, 24)
    dell = Laptop(105, "Dell", 2012, 2299, 15)
    print(macbookPro)
    print()
    print(dell)
    print()
    print(asus)


main()
