import time

from utils import ACoord, Logger
from sprite import Sprite
from dino import Dino
from cactus import Cactus

# filu = open("log.txt", 'w')
#
# def log(*args):
#     global filu
#     print(*args, file=filu)
#


class ScreenPrinter:
    def __init__(self, path_to_background, term_dim_x=100, term_dim_y=24):
        self.term_dim_x = term_dim_x
        self.term_dim_y = term_dim_y

        self.sprites = []

        try:
            with open(path_to_background, 'r') as file:
                raw_data = file.read()
        except FileNotFoundError:
            raise FileNotFoundError("Invalid filepath!")

        lines = raw_data.split("\n")
        temp_buffer = {}

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                temp_buffer[x, y,] = lines[y][x]
                # temp_buffer[x, y,] = f"{y % 10}"

        dim_x = len(lines[0])
        dim_y = len(lines) - 1

        self.__current_buffer = temp_buffer

    def changeCharacterAtPos(self, pos_x, pos_y, char, safe=True):
        if len(char) != 1 and safe:
            raise Exception("Invalid char!")


        if not ( 0 <= pos_x < self.term_dim_x or 0 <= pos_y < self.term_dim_y):
            raise Exception("Invalid arguments!")

        self.getCurrentScreenBuffer()[pos_x, pos_y] = char

    def commit(self):
        print("\033[F" * (self.term_dim_y + 2), end="", flush=False)

        for y in range(self.term_dim_y):
            for x in range(self.term_dim_x):
                print(self.__current_buffer[x, y,], end="")
            print()

    def getCurrentScreenBuffer(self):
        return self.__current_buffer

    def drawSprite(self, pos_x, pos_y, spr):
        for y in range(spr.dim_y):
            for x in range(spr.dim_x):
                log(x, y)
                self.changeCharacterAtPos(pos_x + x, pos_y + y, spr.getCurrentScreenBuffer()[x, y,])

    def attachSprite(self, spr):
        self.sprites.append(spr)
        spr.setScreenPrinter(self)

    def updateSprites(self):
        for i in self.sprites:
            i.object.update()


# filu.close()
