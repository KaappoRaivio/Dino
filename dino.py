from pynput import keyboard
from sprite import Sprite

import time

class Dino:
    def __init__(self, spr, strength=6, gravity=2, pos_x=6, pos_y=12, collision_logic=True, framerate=4):

        self.spr = spr
        self.spr.attachToObject(self)
        self.spr.draw(pos_x, pos_y)

        self.strength = strength
        self.gravity = gravity
        self.height = 0
        self.speed = 0
        self.collision_logic = collision_logic

        self.framerate = framerate


        self.down_held = False
        self.up_held = False

        self.in_air = False
        self.__in_air_reference = True
        self.__frame = 0

        def _onPress(key):

            try: k = key.char # single-char keys
            except: k = key.name # other keys

            self.spr.screenPrinter.log(f"Tomii! {self.__frame}")


            if k in ['up', 'space', 'w']: # hyppy
                self.endCrouch()
                self.jump()

            if k in ['down', 's']:
                if not self.pos_y - self.spr.dim_y == 0:
                    self.speed = -5
                self.startCrouch()

            return True

        def _onRelease(key):

            try: k = key.char # single-char keys
            except: k = key.name # other keys


            if k in ['down', 's']:
                self.endCrouch()

            return True

        self.listener = keyboard.Listener(on_press=_onPress, on_release=_onRelease)
        self.listener.start()

    def __del__(self):
        # del self.spr
        del self

    def getUpdateFrame(self):
        if self.in_air is not self.__in_air_reference:
            self.__in_air_reference = self.in_air
            self.__frame = 1
            return True
        else:
            self.__frame += 1
            return self.__frame % self.framerate == 0



    def setSelfToAir(self):
        self.in_air = True

    def setSelfToGround(self):
        self.in_air = False

    def jump(self):
        if self.height == 0:
            self.in_air = True
            self.speed = self.strength

    def startCrouch(self):
        self.spr.updateSprite(Sprite.prepareBuffer(open("resources/dino/dino_crouched.txt").read()))


    def endCrouch(self):
        self.spr.updateSprite(Sprite.prepareBuffer(open("resources/dino/dino.txt").read()))






    def update(self):
        if not self.listener.is_alive():
            self.listener.start()

        if self.getUpdateFrame():
            self.height += self.speed
            self.spr.move(0, -self.speed)
            self.speed -= self.gravity

        if self.pos_y + self.spr.dim_y > self.spr.screenPrinter.term_dim_y:
            self.spr.moveAbsolute(self.pos_x, self.spr.screenPrinter.term_dim_y - self.spr.dim_y - 2)
            self.height = 0
            self.speed = 0

        if self.height <= 0:
            self.in_air = False
            self.speed = 0



    def checkForCollisions(self):
        if not self.collision_logic:
            return False

        for candinate in self.spr.screenPrinter.collision_matrix:
            for pos, char in self.spr.getCurrentScreenBuffer().items():
                if char == self.spr.getTransparentChar():
                    continue

                abs_pos = (pos[0] + self.pos_x , pos[1] + self.pos_y)

                if abs_pos == candinate:
                    self.spr.screenPrinter.collision_matrix = []
                    return True
        else:
            self.spr.screenPrinter.collision_matrix = []
            return False

    @property
    def pos_x(self):
        return self.spr.pos_x
        # return 4

    @property
    def pos_y(self):
        return self.spr.pos_y
        # return 42

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = int(val + 0.5)




    @pos_x.setter
    def pos_x(self, val):
        raise Exception("not a chance")




    @pos_y.setter
    def pos_y(self, val):
        raise Exception("not a chance")
