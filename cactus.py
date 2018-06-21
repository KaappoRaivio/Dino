class Cactus:
    def __init__(self, spr, pos_y=16):

        self.spr = spr
        spr.attachToObject(self)

        self.pos_y = pos_y
        # self.spr.draw(6, )
        self.spr.draw(self.spr.screenPrinter.term_dim_x, self.pos_y)
        self.pos_x = self.spr.screenPrinter.term_dim_x

    def update(self):
        self.spr.move(-5, 0)
        self.pos_x -= 5

        if self.pos_x < -3:
                del self

    def __del__(self):
        self.spr.undraw()
        del self
