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

            # if key == keyboard.Key.esc: return False # stop listener

            if k in ['up', 'space']: # keys interested
                self.jump()
                self.endCrouch()

            if k in ['down']:
                self.startCrouch()

        def _onRelease(key):

            try: k = key.char # single-char keys
            except: k = key.name # other keys

            # if key == keyboard.Key.esc: return False # stop listener

            if k in ['down']:
                self.endCrouch()

        lis = keyboard.Listener(on_press=_onPress, on_release=_onRelease)
        lis.start()

    def jump(self):
        if self.height == 0:
            self.speed = self.strength

    def startCrouch(self):
        self.spr.updateSprite(Sprite.prepareBuffer(open("crouched.txt").read()))


    def endCrouch(self):
        self.spr.updateSprite(Sprite.prepareBuffer(open("dino.txt").read()))






    def update(self):
        self.height += self.speed
        self.spr.move(0, -self.speed)
        self.speed -= self.gravity

        self.pos_x = self.spr.pos_x
        self.pos_y = self.spr.pos_y


        # if self.height < 0:
        #     self.height = 0
        #     self.spr.move(6, 12)

        if self.height == 0:
            self.speed = 0

    def checkForCollisions(self):
        if not self.collision_logic:
            return False
        # for other in self.spr.screenPrinter.sprites:
        #     if other is self.spr:
        #         continue
        #
        #     for selfpos in self.spr.getCurrentScreenBuffer():
        #         for otherpos in other.getCurrentScreenBuffer():
        #             absselfpos = (selfpos[0] + self.pos_x, selfpos[1] + self.pos_y)
        #             absotherpos = (otherpos[0] + other.pos_x, otherpos[1] + other.pos_y)
        #
        #             if absselfpos == absotherpos:
        #
        #                 print(f"Collision:\n\t{other} with {self}, pos: {selfpos}, charself: {self.spr.getCurrentScreenBuffer()[selfpos]}, charother: {other.getCurrentScreenBuffer()[otherpos]}")
        #                 # self.spr.screenPrinter.changeCharacterAtPos(*selfpos, '\033[31m \033[37m', safe=False)
        #                 self.spr.screenPrinter.changeCharacterAtPos(*selfpos, 'asd', safe=False)
        #
        #                 return True
        # else:
        #     return False

        # for other in self.spr.screenPrinter.sprites:
        #     if other is self.spr:
        #         continue
        #     if (3 <= other.pos_x <= 21) and self.pos_y >= self.spr.screenPrinter.term_dim_y - 15:
        #         return True

        for candinate in self.spr.screenPrinter.collision_matrix:
            for pos, char in self.spr.getCurrentScreenBuffer().items():
                abs_pos = (pos[0] + self.pos_x - 3 , pos[1] + self.pos_y)

                # if char == self.spr.getTransparentChar():
                #     continue

                if abs_pos == candinate:
                    self.spr.screenPrinter.collision_matrix = []
                    return True
        else:
            self.spr.screenPrinter.collision_matrix = []
            return False
