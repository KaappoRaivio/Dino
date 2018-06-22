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

        self.reportCollision()

        if self.pos_x < -5: # Over the screen border
                self.spr.screenPrinter.sprites.remove(self.spr)
                del self.spr
                del self

    # def __del__(self):
    #     self.cacti.remove(self)
    #     self.spr.undraw()
    #     del self

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val):
        self.__speed = int(val)

    @classmethod
    def changeSpeed(cls, new_speed):
        for cactus in cls.cacti:
            cactus.speed = new_speed

    def reportCollision(self):
        for coordinate, char in self.spr.getCurrentScreenBuffer().items():

            coordinate = (coordinate[0] + self.spr.pos_x, coordinate[1] + self.pos_y) #convertabsolute

            if char == self.spr.getTransparentChar():
                continue
            else:
                if coordinate not in self.spr.screenPrinter.collision_matrix:
                    self.spr.screenPrinter.collision_matrix.append(coordinate)
                else:
                    print("Expected collision!")
