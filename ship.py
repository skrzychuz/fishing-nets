import pygame


class Ship():

    def __init__(self, screen):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image_right = pygame.image.load('../images/ship_right.bmp')
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right

        self.rect = self.image_right.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center_position = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update_ship_position(self):
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center_position -= 1.5
            self.image = self.image_left

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_position += 1.5
            self.image = self.image_right

        self.rect.centerx = self.center_position

    def draw_ship(self):
        self.screen.blit(self.image, self.rect)
