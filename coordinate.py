class NotImplementedError(Exception):
    pass

class RCoord:
    def __init__(self, delta_x, delta_y):
        self.x = delta_x
        self.y = delta_y

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f"rel({self.x}, {self.y})"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if val > 8:
            self.__x = 8
        elif val < -8:
            self.__x = -8
        else:
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if val > 8:
            self.__y = 8
        elif val < -8:
            self.__y = -8
        else:
            self.__y = val

    def __add__(other, self):
        if isinstance(other, RCoord):
            return ACoord(self.x + other.x, self.y + other.y)
        elif isinstance(other, ACoord):
            print("# WARNING: u sure m8 u want to add two absolute coordinates")
            return ACoord(self.x + other.x, self.y + other.y)
        else:
            raise NotImplementedError


class ACoord:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f"abs({self.x}, {self.y})"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if val > 8:
            self.__x = 8
        elif val < -8:
            self.__x = -8
        else:
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if val > 8:
            self.__y = 8
        elif val < -8:
            self.__y = -8
        else:
            self.__y = val

    def __add__(self, other):
        if isinstance(other, RCoord):
            return ACoord(self.x + other.x, self.y + other.y)
        elif isinstance(other, ACoord):
            print("# WARNING: u sure m8 u want to add two absolute coordinates")
            return ACoord(self.x + other.x, self.y + other.y)
        else:
            raise NotImplementedError
