import sys
import pygame

from fishing_net import Fishing_Net


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


def screen_update(settings, screen, ship, nets):
    screen.fill(settings.bg_color)
    for net in nets.sprites():
        net.draw_net()
    ship.draw_ship()
    pygame.display.flip()

def update_nets_number(nets):
    for net in nets.copy():
        if net.rect.bottom <= 0:
            nets.remove(net)

def fire(settings, screen, ship, nets):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if settings.net_limit > 0:
        net = Fishing_Net(settings, screen, ship)
        nets.add(net)
        settings.net_limit -= 1
        settings.net_width -= 2
