import sys
import pygame
from pygame.sprite import Group

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

    fun.create_row(settings, screen, fishes)

    pygame.display.set_caption("One Hundred Fishing Nets")
    while True:
        fun.check_events(settings, screen, ship, nets)
        if settings.game_active:
            ship.update_ship_position()
            nets.update()
            fun.update_fishes(settings, fishes)
            fun.update_nets_number(settings, nets, fishes, screen)
        else:
            # Create TextInput-object
            textinput = pygame_textinput.TextInput()

            screen = pygame.display.set_mode((1200, 800))
            clock = pygame.time.Clock()

            while True:
                screen.fill((225, 225, 225))

                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        exit()

                # Feed it with events every frame
                textinput.update(events)
                # Blit its surface onto the screen
                screen.blit(textinput.get_surface(), (10, 10))

                pygame.display.update()
                clock.tick(30)



        fun.screen_update(settings, screen, ship, nets, fishes)


run_game()
