import pygame
import sys
from pygame.locals import *
import math

ANCHO = 640
LARGO = 480

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, LARGO), 0, 32)

pxarray = pygame.PixelArray(pantalla)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        pantalla.fill((0,0,0))

        for y, py in enumerate(pxarray):
            for x, px in enumerate(py):
                if int(x) == (int(y)*int(y)) - 30*int(y) +450:
                    pxarray[y][x] = 0xFFFFFF

        pygame.display.update()

color = 255, 0, 0
first = True
prev_x, prev_y = 0, 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((0,0,0))

    for y, py in enumerate(pxarray):
        for x, px in enumerate(py):
            if int(x) == (int(y)*int(y)) - 30*int(y) +450:
                pxarray[y][x] = 0xFFFFFF

                if first:
                    first = False
                    prev_x, prev_y = x,y
                    continue

                pygame.draw.line(pantalla, color, (prev_y, prev_x), (y, x))
                prev_x, prev_y = x, y

    first = True
    pygame.display.flip()
                    

