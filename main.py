DINO_STRENGTH = 6
DINO_GRAVITY = 2
DINO_FRAMERATE = 4
DINO_COLLISION_LOGIC = True


CACTUS_PROBABILITY = 2 # in percents per frame
CACTUS_SPAWN_GAIN = 0.0001

PTEROSAUR_PROBABILITY = 1
PTEROSAUR_SPAWN_GAIN = 0.0001

WINDOW_DIM_X = 229
WINDOW_DIM_Y = 52

FRAMERATE = 60

SPEED_GAIN = 0.01

import time
import random

from sprite import Sprite
from dino import Dino
from cactus import Cactus
from ScreenPrinter import ScreenPrinter
from pterosaur import Pterosaur
from color import colors
# from highscorehandler import ServerHandler


printer = ScreenPrinter("background.txt", term_dim_x=WINDOW_DIM_X, term_dim_y=WINDOW_DIM_Y)
dino_spr = Sprite.fromFilePath("resources/dino/dino.txt")


printer.attachSprite(dino_spr)
dino = Dino(dino_spr,
            strength=DINO_STRENGTH,
            gravity=DINO_GRAVITY,
            pos_y=WINDOW_DIM_Y - 12,
            collision_logic=DINO_COLLISION_LOGIC,
            framerate=DINO_FRAMERATE)


cactus_sprites = []
cacti = []
pterosaurs = []

counter = 0
latest = 0

cactus_spacer_float = 50.0
pterosaur_spacer_float = 50.0

speed = 3


def makeCactus(printer, path):
    temp_sprite = Sprite.fromFilePath(path)
    printer.attachSprite(temp_sprite)
    return Cactus(temp_sprite, speed=-5)


def makePterosaur(printer, path):
    temp_sprite = Sprite.fromFilePath(path)
    printer.attachSprite(temp_sprite)
    return Pterosaur(temp_sprite, speed=-5)



# cacti.append(makeCactus(printer, "resources/cactus/cactus.txt"))
# pterosaurs.append(makePterosaur(printer, "resources/pterosaur/pterosaur1.txt"))

# server_handler = ServerHandler()

while True:
    cactus_spacer_float = max(5, cactus_spacer_float - 0.025)
    cactus_spacer = int(cactus_spacer_float)

    pterosaur_spacer_float = max(20, cactus_spacer_float - 0.025)
    pterosaur_spacer = int(pterosaur_spacer_float)


    printer.commit()
    printer.updateSprites()

    cycle_beginning = time.time()


    if random.randint(0, 100) in list(range(int(CACTUS_PROBABILITY +  CACTUS_SPAWN_GAIN ** counter))) and latest > cactus_spacer:
        cacti.append(makeCactus(printer, "resources/cactus/cactus.txt"))
        latest = -1

    if random.randint(0, 100) in list(range(int(PTEROSAUR_PROBABILITY + PTEROSAUR_SPAWN_GAIN ** counter))) and latest > pterosaur_spacer and counter > 1000:
        pterosaurs.append(makePterosaur(printer, "resources/pterosaur/pterosaur1.txt"))
        latest = -1


    # speed = 20
    speed = int(15 + counter * SPEED_GAIN)
    Cactus.changeSpeed(speed)
    Pterosaur.changeSpeed(speed)

    #speed
    speed_string = f"Speed: {speed}"
    printer.putText(printer.term_dim_x - 20 - len(speed_string), 8, speed_string, color=colors.blackwhite)


    # Score
    scorestring = f"Score: {counter}"

    # Spacer

    spacerstring = f"Spacer: {cactus_spacer}"

    printer.putText(printer.term_dim_x - 5 - len(scorestring), 8, scorestring, color=colors.blackwhite)
    printer.putText(printer.term_dim_x - 35 - len(spacerstring), 8, spacerstring, color=colors.blackwhite)


    cycle_end = time.time()
    cycle_time = cycle_end - cycle_beginning

    time.sleep(max(1 / FRAMERATE - cycle_time, 0))

    if dino.checkForCollisions():
        gameover = Sprite.fromFilePath("resources/misc/gameover.txt")
        printer.attachSprite(gameover)
        gameover.draw(40, 16)
        printer.commit()
#         server_handler.reportScore(counter, input())
#         ServerHandler.stopAllThreads()
        quit()


    counter += 1
    latest += 1

