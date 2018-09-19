import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keydown_events(event, ship)
        if event.type == pygame.KEYUP:
            keyup_events(event, ship)


def keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True


def keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def screen_update(screen, ship, settings):
    screen.fill(settings.bg_color)
    ship.draw_ship()
    pygame.display.flip()
