DINO_STRENGTH = 10
DINO_GRAVITY = 4
CACTUS_PROBABILITY = 5 # in percents per frame

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
dino = Dino(spr, strength=DINO_STRENGTH, gravity=DINO_GRAVITY)

sprites = []
cacti = []

counter = 0

while True:
    if random.randint(0, 100) in list(range(CACTUS_PROBABILITY)):
        sprites.append(Sprite.fromFilePath("obstacle.txt"))
        printer.attachSprite(sprites[-1])
        cacti.append(Cactus(sprites[-1]))

    printer.commit()
    time.sleep(0.05)
    printer.updateSprites()

    counter += 1

    # Score

    for i in range(len(str(counter))):
        printer.changeCharacterAtPos(90 + i, 2, str(counter)[i])

    if dino.checkForCollisions():
        string = "Game over!"
        for i in range(len(string)):
            printer.changeCharacterAtPos(12 + i, 8, string[i])
        printer.commit()
        quit()
