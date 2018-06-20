class Cactus:
    def __init__(self, spr):
        self.spr = spr

        # self.spr.draw(6, )
        self.spr.draw(self.spr.screenPrinter.term_dim_x, 16)
        self.pos_x = self.spr.screenPrinter.term_dim_x

    def update(self):
        self.spr.move(-1, 0)
        self.pos_x -= 1
