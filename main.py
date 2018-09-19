import sys
import pygame as pygame
from settings import Settings
from ship import Ship
import functions as fun


def run_game():
    # # Initialize pygame, settings, and screen object.
    # pygame.init()
    # screen = pygame.display.set_mode(
    #     (ai_settings.screen_width, ai_settings.screen_height))
    # pygame.display.set_caption("my game")
    #
    # # Make the Play button.
    # play_button = Button(ai_settings, screen, "Play")
    #
    # # Create an instance to store game statistics, and a scoreboard.
    # stats = GameStats(ai_settings)
    # sb = Scoreboard(ai_settings, screen, stats)
    #
    # # Make a ship, a group of bullets, and a group of aliens.
    # ship = Ship(ai_settings, screen)
    # bullets = Group()
    # aliens = Group()
    #
    # # Create the fleet of aliens.
    # gf.create_fleet(ai_settings, screen, ship, aliens)

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    ship = Ship(screen)

    pygame.display.set_caption("One Hundred Fishing Nets")
    while True:
        fun.check_events(ship)
        ship.update_ship_position()
        fun.screen_update(screen, ship, settings)


run_game()
