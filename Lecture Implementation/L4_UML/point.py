class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def move(self, new_x, new_y):
        if isinstance(new_x, int):
            if isinstance(new_y, int):
                self.__x = new_x
                self.__y = new_y
                return True
            else:
                return False
        else:
            return False

    def reset(self):
        self.__x = 0
        self.__y = 0

    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"