from baseobject import BaseObject
from sprite import Sprite

class Cactus(BaseObject):
    cacti = []

    speed_x_cls = -5
    speed_y = 0
    __frame_counter = 0

    def __init__(self, sprite, speed):
        super().__init__(pos_x=sprite.screenPrinter.term_dim_x, pos_y=44, sprite=sprite, speed_x=speed, speed_y=0, is_movable=True, has_collision_logic=True)
        Cactus.cacti.append(self)

        sprite.attachToObject(self)

        self.speed_x = speed
        self.speed_y = 0



    def update(self):
        if self.getFrameCounter():
            self.updateMoving()

        self.reportCollision()
        self.delIfOverTheEdge()


    def delete(self):
        self.spr.delete()
        del self


    @classmethod
    def getFrameCounter(cls):
        cls.__frame_counter += 1
        return cls.__frame_counter % max(1, 10 + len(cls.cacti) - cls.speed_x_cls) in range(len(cls.cacti))

    @classmethod
    def changeSpeed(cls, new_speed):
        cls.speed_x_cls = new_speed
        for cactus in cls.cacti:
            cactus.speed = new_speed
