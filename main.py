DINO_STRENGTH = 10
DINO_GRAVITY = 2
CACTUS_PROBABILITY = 5 # in percents per frame
WINDOW_DIM_X = 183
WINDOW_DIM_Y = 55



import time
import random

from utils import ACoord, Logger
from sprite import Sprite
from dino import Dino
from cactus import Cactus
from ScreenPrinter import ScreenPrinter




printer = ScreenPrinter("background.txt", term_dim_x=WINDOW_DIM_X, term_dim_y=WINDOW_DIM_Y)
spr = Sprite.fromFilePath("testi.txt")
cacspr = Sprite.fromFilePath("obstacle.txt")

printer.attachSprite(cacspr)
cactus = Cactus(cacspr, pos_y=WINDOW_DIM_Y - 8)

printer.attachSprite(spr)
dino = Dino(spr, strength=DINO_STRENGTH, gravity=DINO_GRAVITY, pos_y=WINDOW_DIM_Y - 12)

sprites = []
cacti = []

counter = 0

while True:
    if random.randint(0, 100) in list(range(CACTUS_PROBABILITY)):
        sprites.append(Sprite.fromFilePath("obstacle.txt"))
        printer.attachSprite(sprites[-1])
        cacti.append(Cactus(sprites[-1], pos_y=WINDOW_DIM_Y - 8))

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
