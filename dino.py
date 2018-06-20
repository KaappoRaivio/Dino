from pynput import keyboard

import time

class Dino:
    def __init__(self, spr, strength=6, gravity=2, pos_x=6, pos_y=12):

        self.spr = spr
        self.spr.attachToObject(self)
        self.spr.draw(pos_x, pos_y)

        self.strength = strength
        self.gravity = gravity
        self.height = 0
        self.speed = 0
        self.pos_x  = pos_x
        self.pos_y = pos_y

        def on_press(key):

            try: k = key.char # single-char keys
            except: k = key.name # other keys

            if key == keyboard.Key.esc: return False # stop listener

            if k in ['up']: # keys interested
                self.jump()


        lis = keyboard.Listener(on_press=on_press)
        lis.start()

    def jump(self):
        if self.height == 0:
            self.speed = self.strength

    def crouch(self):
        pass

    def update(self):
        self.height += self.speed
        self.spr.move(0, -self.speed)
        self.speed -= self.gravity

        # if self.height < 0:
        #     self.height = 0
        #     self.spr.move(6, 12)

        if self.height == 0:
            self.speed = 0

    def checkForCollisions(self):
        for other in self.spr.screenPrinter.sprites:
            if other is self.spr:
                continue

            for selfpos in self.spr.getCurrentScreenBuffer():
                for otherpos in other.getCurrentScreenBuffer():
                    selfpos = (selfpos[0] + self.pos_x, selfpos[1] + self.pos_y)
                    otherpos = (otherpos[0] + other.pos_x, otherpos[1] + other.pos_y)

                    if selfpos == otherpos:
                        print(f"Collision:\n\t{other} with {self}, pos: {selfpos}")
                        return True
        else:
            return False
