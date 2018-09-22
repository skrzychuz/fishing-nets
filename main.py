import sys
import pygame
from pygame.sprite import Group

from fishing_net import Fishing_Net
from settings import Settings
from ship import Ship
import functions as fun


def run_game():

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    ship = Ship(screen)
    nets = Group()

    pygame.display.set_caption("One Hundred Fishing Nets")
    while True:
        fun.check_events(settings, screen, ship, nets)
        ship.update_ship_position()
        nets.update()
        fun.update_nets_number(nets)
        fun.screen_update(settings, screen, ship, nets)


run_game()
