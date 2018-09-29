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
                    screen.fill(settings.bg_color)
                    myfont = pygame.font.Font(None, 40)
                    textsurface = myfont.render("Wait a sec...", True, settings.font_color, settings.bg_color)
                    screen.blit(textsurface, (screen.get_rect().centerx, screen.get_rect().centery))
                    pygame.display.flip()
                    return name
            elif evt.type == QUIT:
                return
        screen.fill(settings.bg_color)
        block_result = font.render("Result: " + str(settings.scores), True,
                                   settings.font_color)
        rect = block_result.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block_result, rect)

        block_name = font.render("Insert Your Name: " + name, True,
                                 settings.font_color)
        rect = block_name.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block_name, (rect.x, rect.y + 50))
        pygame.display.flip()
