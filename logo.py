import pygame


class Logo:
    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.GREEN = (0, 102, 71)
        self.GOLD = (255, 209, 63)
        self.WHITE = (255, 255, 255)

    def draw_rectangles(self):
        pygame.draw.rect(self.main_surface, self.GREEN, (5, 5, 400, 200), 3)
        pygame.draw.rect(self.main_surface, self.GREEN, (10, 10, 390, 190), 0)
        pygame.display.update()

    def draw_trellis(self):
        pygame.draw.polygon(self.main_surface, self.GOLD, ((145, 100), (265, 100), (205, 20)), 3)
        pygame.draw.line(self.main_surface, self.GOLD, (205, 100), (205, 20), 3)
        pygame.draw.line(self.main_surface, self.GOLD, (205, 100), (235, 60), 3)
        pygame.draw.line(self.main_surface, self.GOLD, (205, 100), (175, 60), 3)
        pygame.display.update()

    def draw_words(self):
        myFont = pygame.font.SysFont("Helvetica", 22)
        my_other_Font = pygame.font.SysFont("Helvetica", 18)
        school = myFont.render("SANDY SPRING FRIENDS SCHOOL", 1, self.WHITE)
        motto = my_other_Font.render("Let Your Lives Speak", 1, self.WHITE)
        self.main_surface.blit(school, (75, 120))
        self.main_surface.blit(motto, (135, 150))
        pygame.display.update()

