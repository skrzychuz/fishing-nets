import sys
import pygame

import settings
from fishing_net import Fishing_Net
from fish import Fish


def check_events(settings, screen, ship, nets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keydown_events(event, settings, screen, ship, nets)
        if event.type == pygame.KEYUP:
            keyup_events(event, ship)


def keydown_events(event, settings, screen, ship, nets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire(settings, screen, ship, nets)


def keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def screen_update(settings, screen, ship, nets, fishes):
    screen.fill(settings.bg_color)
    for net in nets.sprites():
        net.draw_net()
    ship.draw_ship()
    fishes.draw(screen)
    pygame.display.flip()



def update_nets_number(settings, nets, fishes, screen):
    for net in nets.copy():
        if net.rect.bottom <= 0:
            nets.remove(net)
    collisions = pygame.sprite.groupcollide(nets, fishes, False, True)
    if len(fishes) == 0:
        create_row(settings,screen, fishes)


def fire(settings, screen, ship, nets):
    if settings.net_limit >= 0:
        net = Fishing_Net(settings, screen, ship)
        nets.add(net)
        settings.net_limit -= 1
        # print(settings.net_limit)
        settings.net_width -= 2
        # print(settings.net_width)
    if settings.net_limit < 0:
        settings.game_active = False


def create_row(settings, screen, fishes):
    new_fish = Fish(settings, screen)
    available_space_x = settings.screen_width - 1.5 * new_fish.rect.width
    number_fish_in_row = int(available_space_x / (1.5 * new_fish.rect.width))
    number_rows = 8

    for row_index in range(number_rows):
        for fish_index in range(number_fish_in_row):
            new_fish = Fish(settings, screen)
            new_fish.x = new_fish.rect.width - 1100 + 1.5 * new_fish.rect.width * fish_index
            new_fish.rect.x = new_fish.x
            new_fish.rect.y = new_fish.y = new_fish.rect.height + 1.5 * new_fish.rect.height * row_index

            fishes.add(new_fish)


def update_fishes(setings, fishes):
    check_row_edges(setings, fishes)
    fishes.update()


def check_row_edges(settings, fishes):
    for fish in fishes.sprites():
        if fish.check_fish_on_edges():
            change_row_direction(settings, fishes)
            break


def change_row_direction(settings, fishes):
    for fish in fishes.sprites():
        fish.rect.y += settings.rows_drop
    settings.rows_direction *= -1
