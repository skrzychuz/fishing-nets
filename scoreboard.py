import json

import pygame
import data as data


class Scoretable():

    def __init__(self, screen):
        self.screen = screen

    def show(self, name, settings):
        self.screen.fill(settings.bg_color)
        myfont = pygame.font.Font(None, 30)
        stringresult = str(settings.scores)
        textsurface = myfont.render(name + ":  " + stringresult, False, (80, 80, 80))
        self.screen.blit(textsurface, (0, 0))
        pygame.display.flip()

    def show2(self, name, settings):
        self.screen.fill(settings.bg_color)
        data.add_score(name, settings.scores)
        json_data = data.get_best_ten()
        myfont = pygame.font.Font(None, 40)
        counter = 0
        score_position = 0

        for item in json_data[0]:
            counter += 1
            json_name = item['name']
            score = item['score']

            textsurface = myfont.render(str(counter) + ". " + json_name + ":  " + str(
                score), True, settings.font_color, settings.bg_color)
            score_position += 40
            self.screen.blit(textsurface, (self.screen.get_rect().centerx -150, score_position))

            pygame.display.flip()
            if counter==10:
                break

