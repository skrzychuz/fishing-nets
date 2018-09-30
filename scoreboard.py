import pygame
from pygame.locals import *
import controller


class Scoretable():

    def __init__(self, screen):
        self.screen = screen

    def show(self, name, settings):
        self.screen.fill(settings.bg_color)
        controller.add_score(name, settings.scores)
        json_data = controller.get_sorted_scores()
        myfont = pygame.font.Font(None, 40)
        counter = 0
        players_list = 0

        for item in json_data:
            counter += 1
            json_name = item['name']
            score = item['score']
            textsurface = myfont.render(str(counter) + ". " + json_name + ":  " + str(
                score), True, settings.font_color, settings.bg_color)
            players_list += 40
            self.screen.blit(textsurface, (self.screen.get_rect().centerx -150, players_list))
            pygame.display.flip()
            if counter==10:
                break

    def name(self, screen, settings):
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
                        myfont = pygame.font.Font(None, 50)
                        textsurface = myfont.render("Wait a sec...", True, settings.font_color, settings.bg_color)
                        screen.blit(textsurface, (screen.get_rect().centerx - 0.5*(textsurface.get_rect().width), screen.get_rect().centery))
                        pygame.display.flip()
                        return name
                elif evt.type == QUIT:
                    return
            screen.fill(settings.bg_color)
            self.result_title(screen, settings, font)
            block_name = font.render("Insert Your Name: " + name, True,
                                     settings.font_color)
            rect = block_name.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(block_name, rect)
            pygame.display.flip()

    def result_title(self, screen, settings, font):
        block_result = font.render("Result: " + str(settings.scores), True,
                                   settings.font_color)
        rect = block_result.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block_result, (rect.x, rect.y - 50))