# import sys
#
# import pygame
# from new.game import Game
#
#
# def check_events(game, ship):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             keydown_events(event, ship)
#         if event.type == pygame.KEYUP:
#             keyup_events(event, ship)
#
#
# def keydown_events(event, ship):
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = True
#     if event.key == pygame.K_LEFT:
#         ship.moving_left = True
#     if event.key == pygame.K_SPACE:
#         new_game = Game()
#         new_game.fire_net()
#
#
# def keyup_events(event, ship):
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     if event.key == pygame.K_LEFT:
#         ship.moving_left = False
