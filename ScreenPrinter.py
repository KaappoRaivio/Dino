from utils import ACoord, Logger

filu = open("log.txt", 'w')

def log(string):
    global filu
    print(string, file=filu)



class ScreenPrinter:
    def __init__(self, term_dim_x=80, term_dim_y=24):
        self.term_dim_x = term_dim_x
        self.term_dim_y = term_dim_y

        self.__current_buffer = {}

        for x in range(term_dim_x):
            for y in range(term_dim_y):
                self.__current_buffer[x, y,] = f"{x % 10}"

    def changeCharacterAtPos(self, pos_x, pos_y, char):
        if len(char) != 1:
            raise Exception("Invalid char!")


        if not ( 0 <= pos_x < self.term_dim_x or 0 <= pos_y < self.term_dim_y):
            raise Exception("Invalid arguments!")

        self.getCurrentScreenBuffer()[pos_x, pos_y] = char

    def commit(self):
        print("\033[F" * (self.term_dim_y + 1), end="")

        for y in range(self.term_dim_y):
            for x in range(self.term_dim_x):
                print(self.__current_buffer[x, y,], end="")
            print()

    def getCurrentScreenBuffer(self):
        return self.__current_buffer

printer = ScreenPrinter()
# printer.changeCharacterAtPos(79, 23, "%")
# printer.getCurrentScreenBuffer()[79, 23] = "%"
printer.commit()

log("terve")


for y in range(24):
    for x in range(80):
        printer.changeCharacterAtPos(x, y, "%")
    printer.commit()
