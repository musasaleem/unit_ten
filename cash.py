# Name : Musa Saleem
# Date: December 11, 2018
# Last Modified: December 11, 2018
# Comments: This builds a 7 layer pyramid all in different colors

import brick
import pygame, sys
from pygame.locals import *

# The colors are located below as well as the height of each brick and the space in between each brick and the total
# number of bricks means the total number of bricks that starts at the bottom which is 13 for this pyramid
GREEN = (0, 255, 0)
GOLD = (255, 209, 63)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE =(0, 0, 255)
INDIGO = (63, 0, 255)
ORANGE = (255, 165, 0)
VIOLET = (238, 130, 238)
SPACE = 5
HEIGHT = 20
x_number_bricks = 13
colors = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]


pygame.init()
mainSurface = pygame.display.set_mode((500, 250), 0, 32)  # Window of pygame
pygame.display.set_caption("Bricks")  # Title

WIDTH = (500 - (x_number_bricks * SPACE))/x_number_bricks  # The formula for finding the width

# Starting value for x and y
x = 0
y = 250 - HEIGHT


for m in range(7):  # 7 for 7 layers and for loop so it loops it
    x = (WIDTH + SPACE) * m  # moves the x
    color = colors[m]    # color function
    for b in range(x_number_bricks):  # another for loop for the number of bricks
        bricks = brick.Brick(WIDTH, HEIGHT, color, mainSurface)   # creating a brick
        bricks.create_a_brick(x, y)                              # creating a brick
        x = x + WIDTH + SPACE                                    # moving the x
        pygame.display.update()                                  # Displaying pygame
    x_number_bricks = x_number_bricks - 2                        # subtracting two bricks from every row
    y = y - HEIGHT - SPACE                                       # centering the pyramid

# Ending loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
