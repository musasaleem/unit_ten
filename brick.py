import pygame

class Brick:
    def __init__(self, width, height, color, main_surface):
        """
        Variables for the brick
        :param width: width of the brick
        :param height: height of the brick
        :param color: color of the brick
        :param main_surface: main surface of the brick
        """
        self.main_surface = main_surface
        self.color = color
        self.height = height
        self.width = width

    def create_a_brick(self, x,y):
        """
        Creates the brick given the variables and coordinates 
        :param x: coordinate
        :param y: coordinate
        :return: displays the bruick
        """
        pygame.draw.rect(self.main_surface, self.color,(x, y, self.width, self.height), 0)
        pygame.display.update()