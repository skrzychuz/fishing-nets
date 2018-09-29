import pygame
from pygame.locals import *


def name(screen, settings):
    name = ""
    font = pygame.font.Font(None, 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    return name
            elif evt.type == QUIT:
                return
        screen.fill(settings.bg_color)
        block = font.render("Result: " + str(settings.scores) + "!!  " + "Insert Your Name: " + name, True,
                            settings.font_color)
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()
