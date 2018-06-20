from pynput import keyboard


class Dino:
    def __init__(self, spr, strength=6, gravity=1):
        self.spr = spr
        self.spr.draw(6, 12)

        self.strength = strength
        self.gravity = gravity
        self.height = 0
        self.speed = 0

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
