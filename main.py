import time
import random

from utils import ACoord, Logger
from sprite import Sprite
from dino import Dino
from cactus import Cactus
from ScreenPrinter import ScreenPrinter




printer = ScreenPrinter("background.txt")
spr = Sprite.fromFilePath("testi.txt")
cacspr = Sprite.fromFilePath("obstacle.txt")

printer.attachSprite(cacspr)
cactus = Cactus(cacspr)

printer.attachSprite(spr)
dino = Dino(spr, strength=10, gravity=4)

sprites = []
cacti = []

counter = 0

while True:
    if random.randint(0, counter**2) > 100 * counter:
        sprites.append(Sprite.fromFilePath("obstacle.txt"))
        printer.attachSprite(sprites[-1])
        cacti.append(Cactus(sprites[-1]))

    printer.commit()
    time.sleep(0.05)
    printer.updateSprites()

    counter += 1

    if dino.checkForCollisions():
        printer.commit()
        quit()
