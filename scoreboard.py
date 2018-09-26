import pygame


class Scoretable():

    def __init__(self, screen):
        self.screen = screen

    def show(self, name, result):
        myfont = pygame.font.Font(None, 30)
        stringresult = str(result)
        textsurface = myfont.render('Some Text' + name + " " + stringresult, False, (80, 80, 80))
        self.screen.blit(textsurface, (0, 0))
        pygame.display.flip()
