import pygame
from pygame.sprite import Sprite

class Fish(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image_right = pygame.image.load('../images/fish_small_r.bmp')
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right

        self.rect = self.image_right.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def draw_fish(self):
        self.screen.blit(self.image, self.rect)

    def check_fish_on_edges(self):
        return self.rect.right >= self.screen.get_rect().right + 1100 or self.rect.left <= -1100

    def update(self):
        if self.settings.rows_direction == 1:
            self.x += 0.7 * self.settings.rows_direction
            self.image = self.image_right
        if self.settings.rows_direction == -1:
            self.x += 0.7 * self.settings.rows_direction
            self.image = self.image_left

        self.rect.x = self.x

