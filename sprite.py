

class Sprite:
    def __init__(self, screenbuffer, dim_x, dim_y, path_to_file="Path not available"):
        self.__current_buffer = screenbuffer
        self.path_to_file = path_to_file
        self.dim_x = dim_x
        self.dim_y = dim_y

        self.underlying = {}
        self.drawn = False

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

        print(dim_x, dim_y)

        return cls(temp_buffer, dim_x, dim_y, path_to_file=path_to_file)

    def getCurrentScreenBuffer(self):
        return self.__current_buffer

    def setScreenPrinter(self, screenPrinter):
        self.screenPrinter = screenPrinter

    def draw(self, pos_x, pos_y):
        if not hasattr(self, "screenPrinter"):
            raise Exception("Don't know which printer to draw in. setScreenPrinter() first.")

        self.pos_x = pos_x
        self.pos_y = pos_y

        for y in range(self.dim_y):
            for x in range(self.dim_x):
                self.underlying[x, y,] = self.screenPrinter.getCurrentScreenBuffer()[x, y,]
                self.screenPrinter.changeCharacterAtPos(pos_x + x, pos_y + y, self.getCurrentScreenBuffer()[x, y,])

        self.drawn = True

    def undraw(self):
        for y in range(self.dim_y):
            for x in range(self.dim_x):
                self.underlying[x, y,] = self.screenPrinter.getCurrentScreenBuffer()[x, y,]
                self.screenPrinter.changeCharacterAtPos(self.pos_x + x, self.pos_y + y, self.underlying[x, y,])

        self.drawn = False

    def move(self, delta_x, delta_y):
        if not self.drawn:
            raise Exception("Cannot move an undrawn sprite!")

        self.undraw()
        self.draw(self.pos_x + delta_x, self.pos_y + delta_y)
