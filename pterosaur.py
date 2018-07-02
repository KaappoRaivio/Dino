from baseobject import BaseObject
from sprite import Sprite
import random

class Pterosaur(BaseObject):
    pterosaurs = []

    speed_x_cls = -5
    speed_y = 0
    __frame_counter = 0

    def __init__(self, sprite, speed):
        super().__init__(pos_x=sprite.screenPrinter.term_dim_x, pos_y=sprite.screenPrinter.term_dim_y - sprite.dim_y - 8 - random.choice([0, 4]), sprite=sprite, speed_x=speed, speed_y=0, is_movable=True, has_collision_logic=True)
        Pterosaur.pterosaurs.append(self)

        sprite.attachToObject(self)

        self.speed_x = speed
        self.speed_y = 0

        self.__frame = 0

    def update(self):
        if self.getFrameCounter():
            self.updateMoving()

        self.reportCollision()

        if self.getNextAnimationFrame() == 1:
            self.spr.updateSprite(Sprite.prepareBuffer(open("resources/pterosaur/pterosaur1.txt").read()))
        else:
            self.spr.updateSprite(Sprite.prepareBuffer(open("resources/pterosaur/pterosaur2.txt").read()))

        self.delIfOverTheEdge()

        # if self.pos_x < self.spr.dim_x + 24:
        #     print("srgoi")
        #     self.spr.delete()

    def getNextAnimationFrame(self):
        self.__frame += 1
        if 0 < self.__frame % 20 <= 10:
            return 1
        else:
            return 0

    def delete(self):
        Pterosaur.pterosaurs.remove(self)
        self.spr.delete()
        del self


    @classmethod
    def getFrameCounter(cls):
        cls.__frame_counter += 1
        return cls.__frame_counter % max(1, 10 + len(cls.pterosaurs) - cls.speed_x_cls) in range(len(cls.pterosaurs))

    @classmethod
    def changeSpeed(cls, new_speed):
        cls.speed_x_cls = new_speed
        for pterosaur in cls.pterosaurs:
            pterosaur.speed = new_speed
