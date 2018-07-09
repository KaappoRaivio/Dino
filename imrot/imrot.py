import sys, math, time
import numpy as np

sys.path.append("..")

from sprite import Sprite
from ScreenPrinter import ScreenPrinter

class RotatingSprite(Sprite):
    def __init__(self, path_to_file):
        try:
            with open(path_to_file, 'r') as file:
                raw_data = file.read()
        except FileNotFoundError:
            raise FileNotFoundError("Invalid filepath!")

        temp_buffer = Sprite.prepareBuffer(raw_data)

        super().__init__(temp_buffer, path_to_file=path_to_file)

    def rotate(self, amount):
        center_x = self.dim_x // 2
        center_y = self.dim_y // 2

        new_buffer = {}

        for x, y in self.getCenterOrientedBuffer():
            dist, theta, = self.cart2pol(x, y)

            theta += np.radians(amount)

            new_x, new_y, = self.pol2cart(dist, theta)

            new_x += round(self.dim_x / 2, 0)
            new_y += round(self.dim_y / 2, 0)

            # print(x, y, new_x, new_y, self.dim_y)

            new_buffer[new_x, new_y] = self.getCurrentScreenBuffer()[x + round(self.dim_x / 2, 0), y + round(self.dim_y / 2, 0)]

        # print(self.getDimensFromScreenbuffer(new_buffer)[1])

        for y in range(self.getDimensFromScreenbuffer(new_buffer)[1]):
            for x in range(self.getDimensFromScreenbuffer(new_buffer)[0]):

                if not (x, y,) in new_buffer:
                    # print("asd")
                    # new_buffer[x, y] = "#"
                    new_buffer[x, y] = self.getTransparentChar()

        # print("noasd")
        self.updateSprite(new_buffer, draw_after=False)




    def getCenterOrientedBuffer(self):
        buffer = {}
        for x, y in self.getCurrentScreenBuffer():
            buffer[x - round(self.dim_x / 2, 0), y - round(self.dim_y / 2, 0)] = self.getCurrentScreenBuffer()[x, y]

        return buffer

    @staticmethod
    def cart2pol(x, y):
        rho = np.sqrt(x ** 2 + y ** 2)
        phi = np.arctan2(y, x)
        return rho, phi,

    @staticmethod
    def pol2cart(rho, phi):
        x = rho * np.cos(phi)
        y = rho * np.sin(phi)
        # print(x, y)
        return int(x + 0.5) if x > 0 else int(x - 0.5), int(y + 0.5) if x > 0 else int(y - 0.5),


# rho, phi = RotatingSprite.cart2pol(0, 5)
# phi += np.radians(90)
# print(RotatingSprite.pol2cart(rho, phi))

# quit()


a = RotatingSprite("asd.txt")


printer = ScreenPrinter("background.txt", term_dim_x=200, term_dim_y=20)


printer.attachSprite(a)
# a.draw(10, 10)
printer.commit()
# quit()


while True:
    a.draw(10, 10)
    printer.commit()
    a.rotate(10)
    time.sleep(1)
