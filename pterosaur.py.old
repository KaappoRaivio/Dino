from sprite import Sprite

class Pterosaur:
    pterosaurea = []

    def __init__(self, spr, pos_y=14, speed=3):
        self.spr = spr
        spr.attachToObject(self)

        self.pos_y = pos_y
        self.spr.draw(self.spr.screenPrinter.term_dim_x, self.pos_y)
        self.pos_x = self.spr.screenPrinter.term_dim_x
        self.speed = speed

        self.__frame = 0

        Pterosaur.pterosaurea.append(self)

    def update(self):
        self.spr.move(-self.speed, 0)
        self.pos_x -= self.speed

        self.reportCollision()

        if self.getNextAnimationFrame() == 1:
            self.spr.updateSprite(Sprite.prepareBuffer(open("resources/pterosaur/pterosaur1.txt").read()))
        else:
            self.spr.updateSprite(Sprite.prepareBuffer(open("resources/pterosaur/pterosaur2.txt").read()))

        if self.pos_x <= -self.spr.dim_y * 3: # Over the screen border
                self.spr.screenPrinter.sprites.remove(self.spr)
                self.spr.undraw()

    @classmethod
    def changeSpeed(cls, new_speed):
        for pterosaur in cls.pterosaurea:
            pterosaur.speed = new_speed


    def getNextAnimationFrame(self):
        self.__frame += 1
        if 0 < self.__frame % 20 <= 10:
            return 1
        else:
            return 0

        # return self.__frame

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val):
        self.__speed = int(val)


    def reportCollision(self):
        if not self.spr.drawn:
            return

        for coordinate, char in self.spr.getCurrentScreenBuffer().items():

            coordinate = (coordinate[0] + self.spr.pos_x, coordinate[1] + self.pos_y) #convertabsolute


            if char == self.spr.getTransparentChar():
                continue
            else:
                if coordinate not in self.spr.screenPrinter.collision_matrix:
                    self.spr.screenPrinter.collision_matrix.append(coordinate)
