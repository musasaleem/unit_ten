import brick
import pygame, sys
from pygame.locals import *


GREEN = (0, 255, 0)
GOLD = (255, 209, 63)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE =(0, 0, 255)
PURPLE = (255, 0, 255)
SPACE = 5
HEIGHT = 20
x_number_bricks = 9


pygame.init()
mainSurface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Bricks")

WIDTH = (500 - (x_number_bricks * SPACE))/x_number_bricks

x = 0
y = 250 - HEIGHT

for b in range(x_number_bricks):
    bricks = brick.Brick(WIDTH, HEIGHT, GREEN, mainSurface)
    bricks.create_a_brick(x, y)
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
