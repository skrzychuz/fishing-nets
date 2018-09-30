import pygame
from pygame.sprite import Sprite


class Fishing_Net(Sprite):

    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.net_width,
                                settings.net_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = settings.net_color
        self.speed_factor = settings.net_speed

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_net(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

