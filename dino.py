from pynput import keyboard
from sprite import Sprite

import time

class Dino:
    def __init__(self, spr, strength=6, gravity=2, pos_x=6, pos_y=12, collision_logic=True):

        self.spr = spr
        self.spr.attachToObject(self)
        self.spr.draw(pos_x, pos_y)

        self.strength = strength
        self.gravity = gravity
        self.height = 0
        self.speed = 0
        self.collision_logic = collision_logic


        self.down_held = False
        self.up_held = False

        def _onPress(key):

            try: k = key.char # single-char keys
            except: k = key.name # other keys


            if k in ['up', 'space']: # hyppy
                self.jump()
                self.endCrouch()

            if k in ['down']:
                self.startCrouch()

            return True

        def _onRelease(key):

            try: k = key.char # single-char keys
            except: k = key.name # other keys


            if k in ['down']:
                self.endCrouch()

            return True

        lis = keyboard.Listener(on_press=_onPress, on_release=_onRelease)
        lis.start()

    def jump(self):
        if self.height == 0:
            self.speed = self.strength

    def startCrouch(self):
        self.spr.updateSprite(Sprite.prepareBuffer(open("resources/dino/dino_crouched.txt").read()))


    def endCrouch(self):
        self.spr.updateSprite(Sprite.prepareBuffer(open("resources/dino/dino.txt").read()))






    def update(self):
        self.height += self.speed
        self.spr.move(0, -self.speed)
        self.speed -= self.gravity

        if self.pos_y + self.spr.dim_y > self.spr.screenPrinter.term_dim_y:
            self.spr.moveAbsolute(self.pos_x, self.spr.screenPrinter.term_dim_y - self.spr.dim_y - 2)
            self.height = 0
            self.speed = 0

        if self.height <= 0:
            self.speed = 0



    def checkForCollisions(self):
        if not self.collision_logic:
            return False

        for candinate in self.spr.screenPrinter.collision_matrix:
            for pos, char in self.spr.getCurrentScreenBuffer().items():
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
