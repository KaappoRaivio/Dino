class Cactus:
    cacti = []

    def __init__(self, spr, pos_y=16, speed=5):

        self.spr = spr
        spr.attachToObject(self)

        self.pos_y = pos_y
        # self.spr.draw(6, )
        self.spr.draw(self.spr.screenPrinter.term_dim_x, self.pos_y)
        self.pos_x = self.spr.screenPrinter.term_dim_x
        self.speed = speed

        Cactus.cacti.append(self)

    def update(self):
        self.spr.move(-self.speed, 0)
        self.pos_x -= self.speed

        if self.pos_x < -3:
                print("moi")
                del self

    # def __del__(self):
    #     self.spr.undraw()
    #     del self

    @classmethod
    def changeSpeed(cls, new_speed):
        for cactus in cls.cacti:
            cactus.speed = new_speed
