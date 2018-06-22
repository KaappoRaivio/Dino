import time

class Sprite:
    __transparent_char = "§"
    ID = 0

    @classmethod
    def setTransparentChar(cls, val):
        if not isinstance(val, str):
            raise Exception("Not a string!")

        cls.__transparent_char = val

    @classmethod
    def getTransparentChar(cls):
        return cls.__transparent_char

    @staticmethod
    def getDimensFromScreenbuffer(screenbuffer):
        max_x = 0
        max_y = 0

        for i in screenbuffer:
            if i[0] > max_x:
                max_x = i[0]
            if i[1] > max_y:
                max_y = i[1]

        return max_x, max_y,


    def __init__(self, screenbuffer, dim_x, dim_y, path_to_file="Path not available"):
        self.__current_buffer = screenbuffer
        self.path_to_file = path_to_file

        self.dim_x, self.dim_y = Sprite.getDimensFromScreenbuffer(screenbuffer)

        self.underlying = {}
        self.drawn = False

        self.ID += 1
        self.__ID = self.ID

    def __str__(self):
        return f"Sprite('{self.path_to_file}')"

    @classmethod
    def fromFilePath(cls, path_to_file):
        try:
            with open(path_to_file, 'r') as file:
                raw_data = file.read()
        except FileNotFoundError:
            raise FileNotFoundError("Invalid filepath!")

        lines = raw_data.split("\n")
        temp_buffer = {}

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                temp_buffer[x, y,] = lines[y][x]

        dim_x = len(lines[0])
        dim_y = len(lines) - 1


        return cls(temp_buffer, dim_x, dim_y, path_to_file=path_to_file)

    def getCurrentScreenBuffer(self):
        return self.__current_buffer

    def setScreenPrinter(self, screenPrinter):
        self.screenPrinter = screenPrinter

    def draw(self, pos_x, pos_y):
        if not hasattr(self, "screenPrinter"):
            raise Exception("Don't know which printer to draw in. setScreenPrinter() first.")
        if self.drawn:
            raise Exception("Cannot draw twice!")

        self.pos_x = pos_x
        self.pos_y = pos_y

        for y in range(self.dim_y):
            for x in range(self.dim_x):

                if not (0 <= self.pos_x + x < self.screenPrinter.term_dim_x) or not (0 <= self.pos_y + y < self.screenPrinter.term_dim_y):
                    self.underlying[x, y,] = self.getTransparentChar()
                    continue

                if self.getCurrentScreenBuffer()[x, y,] == self.getTransparentChar(): # Transparency
                    self.underlying[x, y,] = self.getTransparentChar()
                    continue


                self.underlying[x, y,] = self.screenPrinter.getCurrentScreenBuffer()[self.pos_x + x, self.pos_y + y,]
                self.screenPrinter.changeCharacterAtPos(pos_x + x, pos_y + y, self.getCurrentScreenBuffer()[x, y,])

        self.drawn = True

    def undraw(self):
        if not self.drawn:
            raise Exception("Cannot undraw twice!")
        for y in range(self.dim_y):
            for x in range(self.dim_x):
                if self.getCurrentScreenBuffer()[x, y,] == self.getTransparentChar():
                    continue
                else:
                    self.screenPrinter.changeCharacterAtPos(self.pos_x + x, self.pos_y + y, self.underlying[x, y,])

        self.underlying = {}
        self.drawn = False

    def move(self, delta_x, delta_y):
        if not self.drawn:
            raise Exception("Cannot move an undrawn sprite!")

        self.undraw()
        self.draw(self.pos_x + delta_x, self.pos_y + delta_y)

    def moveAbsolute(self, x, y):
        if not self.drawn:
            raise Exception("Cannot move an undrawn sprite!")

        self.undraw()
        self.draw(x, y)

    def attachToObject(self, obj):
        self.object = obj

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, val):
        self.__pos_x = int(val)

    @property
    def pos_y(self):
        return self.__pos_y

    @pos_y.setter
    def pos_y(self, val):
        self.__pos_y = int(val)


path_to_file = "dino.txt"

try:
    with open(path_to_file, 'r') as file:
        raw_data = file.read()
except FileNotFoundError:
    raise FileNotFoundError("Invalid filepath!")

lines = raw_data.split("\n")
temp_buffer = {}

for y in range(len(lines)):
    for x in range(len(lines[y])):
        temp_buffer[x, y,] = lines[y][x]

print(Sprite.getDimensFromScreenbuffer(temp_buffer))
