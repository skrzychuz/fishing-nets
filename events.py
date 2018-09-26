import sys

import pygame

def check_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keydown_events(event, game)
        if event.type == pygame.KEYUP:
            keyup_events(event, game)


def keydown_events(event, game):
    if event.key == pygame.K_RIGHT:
        game.ship.moving_right = True
    if event.key == pygame.K_LEFT:
        game.ship.moving_left = True
    if event.key == pygame.K_SPACE:
        game.fire_net()


def keyup_events(event, game):
    if event.key == pygame.K_RIGHT:
        game.ship.moving_right = False
    if event.key == pygame.K_LEFT:
        game.ship.moving_left = False
