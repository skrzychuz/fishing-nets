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
        data.add_score(name, settings.scores)
        json_data = data.get_best_ten()

        for item in json_data['scores']:
            name = item['name']
            score = item['score']

        # myfont = pygame.font.Font(None, 30)
        # textsurface = myfont.render(name + ":  " + stringresult, False, (80, 80, 80))
        # textrect = text.get_rect()
        # textrect.centerx = screen.get_rect().centerx
        # textrect.centery = screen.get_rect().centery
        #
        # screen.fill((255, 255, 255))
        # screen.blit(text, textrect)
        #
        # pygame.display.update()
        #
        #
        #
        #
        #
        #
        # self.screen.fill(settings.bg_color)
        # myfont = pygame.font.Font(None, 30)
        # stringresult = str(settings.scores)
        # textsurface = myfont.render(name + ":  " + stringresult, False, (80, 80, 80))
        # self.screen.blit(textsurface, (0, 0))
        # pygame.display.flip()


    # def save_scores(self):
    #     sd = SortedDict()
    #     sd['c'] = 3
    #     sd['a'] = 1
    #     sd['b'] = 2