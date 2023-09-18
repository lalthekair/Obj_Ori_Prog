from point import Point


def main():
    p1 = Point(12, 20)
    print(p1)
    if p1.move(6, 0):
        print(p1)
    if p1.move('A', 19):
        print(p1)
    p1.reset()
    print(p1)


main()
