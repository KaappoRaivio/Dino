DINO_STRENGTH = 10
DINO_GRAVITY = 2
CACTUS_PROBABILITY = 1 # in percents per frame
SPAWN_GAIN = 0.0005
WINDOW_DIM_X = 204
WINDOW_DIM_Y = 52
CACTUS_MAX_SPEED = 4
CACTUS_MIN_SPEED = 2
FRAMERATE = 60
SPEED_GAIN = 0.00001


import time
import random

from utils import ACoord, Logger
from sprite import Sprite
from dino import Dino
from cactus import Cactus
from ScreenPrinter import ScreenPrinter




printer = ScreenPrinter("background.txt", term_dim_x=WINDOW_DIM_X, term_dim_y=WINDOW_DIM_Y)
spr = Sprite.fromFilePath("dino.txt")
cacspr = Sprite.fromFilePath("obstacle.txt")

printer.attachSprite(spr)
dino = Dino(spr, strength=DINO_STRENGTH, gravity=DINO_GRAVITY, pos_y=WINDOW_DIM_Y - 12, collision_logic=True)

sprites = []
cacti = []

counter = 0
latest = 0

speed = 3


# while True:
#     dino.startCrouch()
#     printer.commit()
#     printer.updateSprites()
#     dino.endCrouch()
#     printer.commit()
#     printer.updateSprites()
#     print("moi")

while True:
    cycle_beginning = time.time()


    if random.randint(0, 100) in list(range(int(CACTUS_PROBABILITY * counter ** SPAWN_GAIN))) and latest > 6:

        sprites.append(Sprite.fromFilePath("obstacle.txt"))
        printer.attachSprite(sprites[-1])
        cacti.append(Cactus(sprites[-1], pos_y=WINDOW_DIM_Y - 8))

        speed += int(counter ** 1.2 * SPEED_GAIN)
        # Cactus.changeSpeed(random.randint(CACTUS_MIN_SPEED, CACTUS_MAX_SPEED))
        Cactus.changeSpeed(speed)

        latest = -1

    # print(printer.collision_matrix)

    printer.commit()
    printer.updateSprites()

    counter += 1
    latest += 1

    # Score
    scorestring = f"Score: {counter}"

    printer.putText(printer.term_dim_x - 5 - len(scorestring), 8, scorestring)

    if dino.checkForCollisions():
        printer.putText(12, 8, "Game over!")
        printer.commit()
        quit()

    cycle_end = time.time()
    cycle_time = cycle_end - cycle_beginning

    time.sleep(max(1 / FRAMERATE - cycle_time, 0))
