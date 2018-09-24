import sys
import pygame
from pygame.sprite import Group

import player
from Scores import Scores
from fish import Fish
from fishing_net import Fishing_Net
from settings import Settings
from ship import Ship
import functions as fun
import pygame_textinput


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    ship = Ship(screen)
    nets = Group()
    fishes = Group()
    score = Scores(settings, screen)

    fun.create_row(settings, screen, fishes)

    pygame.display.set_caption("One Hundred Fishing Nets")
    while True:
        fun.check_events(settings, screen, ship, nets)
        if settings.game_active:
            ship.update_ship_position()
            nets.update()
            fun.update_fishes(settings, fishes)
            fun.update_nets_number(settings, nets, fishes, screen, score)

        else:
            name = player.name()
            dupa = 5

        fun.screen_update(settings, screen, ship, nets, fishes, score)


run_game()
