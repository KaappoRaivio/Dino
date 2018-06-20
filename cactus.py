class Cactus:
    def __init__(self, spr):

        self.spr = spr
        spr.attachToObject(self)

        # self.spr.draw(6, )
        self.spr.draw(self.spr.screenPrinter.term_dim_x, 16)
        self.pos_x = self.spr.screenPrinter.term_dim_x

    def update(self):
        self.spr.move(-5, 0)
        self.pos_x -= 5

        if self.pos_x < -3:
                del self

    def __del__(self):
        self.spr.undraw()
        del self
