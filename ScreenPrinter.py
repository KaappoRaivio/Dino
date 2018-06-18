


screenbuffer = {}

for x in range(24):
    for y in range(80):
        screenbuffer[x, y,] = f"{x*y % 10}"

def printBuffer(screenbuffer, term_dim_x=80, term_dim_y=24):
    print("\033[F" * (term_dim_y + 1), end="")

    for x in range(24):
        for y in range(80):
            print(screenbuffer[x, y,], end="")
        print()

printBuffer(screenbuffer)


class ScreenPrinter:
    def __init__(self, term_dim_x=80, term_dim_y=24):
        self.term_dim_x = term_dim_x
        self.term_dim_y = term_dim_y

        self.__currentBuffer = {}

        for x in range(term_dim_y:
            for y in range(term_dim_x):
                screenbuffer[x, y,] = f"{x*y % 10}"

    def changeCharacterAtPos(self, )

    def getCurrentScreenBuffer(self):
        return self.__currentBuffer
