DINO_STRENGTH = 6
DINO_GRAVITY = 1
CACTUS_PROBABILITY = 1 # in percents per frame
SPAWN_GAIN = 0.05
WINDOW_DIM_X = 229
WINDOW_DIM_Y = 52
CACTUS_MAX_SPEED = 4
CACTUS_MIN_SPEED = 2
FRAMERATE = 20
SPEED_GAIN = 0.01


import time
import random

from utils import ACoord, Logger
from sprite import Sprite
from dino import Dino
from cactus import Cactus
from ScreenPrinter import ScreenPrinter
from pterosaur import Pterosaur



printer = ScreenPrinter("background.txt", term_dim_x=WINDOW_DIM_X, term_dim_y=WINDOW_DIM_Y)
dino_spr = Sprite.fromFilePath("resources/dino/dino.txt")
cactus_spr = Sprite.fromFilePath("resources/cactus/cactus.txt")

printer.attachSprite(dino_spr)
dino = Dino(dino_spr, strength=DINO_STRENGTH, gravity=DINO_GRAVITY, pos_y=WINDOW_DIM_Y - 12, collision_logic=True)

sprites = []
cacti = []

counter = 0
latest = 0

speed = 3

def makeCactus(screen_printer, path):
    temp_sprite = Sprite.fromFilePath(path)
    screen_printer.attachSprite(temp_sprite)
    return Cactus(temp_sprite, pos_y=WINDOW_DIM_Y - 8)

def makePterosaur(screen_printer, path):
    temp_sprite = Sprite.fromFilePath(path)
    screen_printer.attachSprite(temp_sprite)
    return Pterosaur(temp_sprite, pos_y=WINDOW_DIM_Y - 12)

pterosaurs = []

while True:
    cycle_beginning = time.time()



    if random.randint(0, 100) in list(range(int(CACTUS_PROBABILITY + counter * SPAWN_GAIN))) and latest > 6:
        cacti.append(makeCactus(printer, "resources/cactus/cactus.txt"))
        pterosaurs.append(makePterosaur(printer, "resources/pterosaur/pterosaur1.txt"))
        # sprites.append(Sprite.fromFilePath("resources/cactus/cactus.txt"))
        # printer.attachSprite(sprites[-1])
        # cacti.append(Cactus(sprites[-1], pos_y=WINDOW_DIM_Y - 8))


        latest = -1

    speed = int(5 + counter * SPEED_GAIN)
    Cactus.changeSpeed(speed)



    printer.commit()
    printer.updateSprites()

    counter += 1
    latest += 1

    #speed
    speed_string = f"Speed: {speed}"
    printer.putText(printer.term_dim_x - 20 - len(speed_string), 8, speed_string)


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
