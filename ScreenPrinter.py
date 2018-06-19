import time

from utils import ACoord, Logger
from sprite import Sprite

filu = open("log.txt", 'w')

def log(*args):
    global filu
    print(*args, file=filu)



class ScreenPrinter:
    def __init__(self, term_dim_x=80, term_dim_y=24):
        self.term_dim_x = term_dim_x
        self.term_dim_y = term_dim_y

        self.__current_buffer = {}

        self.sprites = []

        for x in range(term_dim_x):
            for y in range(term_dim_y):
                self.__current_buffer[x, y,] = f" "

    def changeCharacterAtPos(self, pos_x, pos_y, char):
        if len(char) != 1:
            raise Exception("Invalid char!")


        if not ( 0 <= pos_x < self.term_dim_x or 0 <= pos_y < self.term_dim_y):
            raise Exception("Invalid arguments!")

        self.getCurrentScreenBuffer()[pos_x, pos_y] = char

    def commit(self):
        print("\033[F" * (self.term_dim_y + 2), end="")

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





printer = ScreenPrinter()
spr = Sprite.fromFilePath("testi.txt")

# printer.drawSprite(5, 5, spr)
printer.attachSprite(spr)
spr.draw(5, 5)

printer.commit()

time.sleep(1)

spr.move(10, 10)
printer.commit()
