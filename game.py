from time import sleep

import pygame
from pygame.sprite import Group

import player
from fish import Fish
from fishing_net import Fishing_Net
from scoreboard import Scoretable
from scores_on_screen import Scores
from ship import Ship
from settings import Settings
import events as event


class Game():

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self.screen)
        self.fish = Fish(self.settings, self.screen)
        self.score_instance = Scores(self.settings, self.screen)
        self.fishes = Group()
        self.nets = Group()
        self.fishing_net = Fishing_Net(self.settings, self.screen, self.ship)
        self.scoretable = Scoretable(self.screen)

    def run_game(self):
        pygame.display.set_caption("One Hundred Fishing Nets")
        self.create_fishes_row()

        while True:
            event.check_events(self)

            if self.settings.game_active:
                self.update_fishes()
                self.nets.update()
                self.update_nets_number()
                self.screen_update()
            else:
                name = player.name(self.screen, self.settings)
                self.screen.fill(self.settings.font_color)
                self.scoretable.show2(name, self.settings)

                sleep(5)
                break


    def screen_update(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.update_ship_position()
        self.ship.draw_ship()
        self.fishes.draw(self.screen)
        self.score_instance.show_score()
        for net in self.nets.sprites():
            net.draw_net()
        pygame.display.flip()

    def create_fishes_row(self):
        available_space_x = self.settings.screen_width - 1.5 * self.fish.rect.width
        number_fish_in_row = int(available_space_x / (1.5 * self.fish.rect.width))
        number_rows = 8

        for row_index in range(number_rows):
            for fish_index in range(number_fish_in_row):
                new_fish = Fish(self.settings, self.screen)
                new_fish.x = new_fish.rect.width - 1100 + 1.5 * new_fish.rect.width * fish_index
                new_fish.rect.x = new_fish.x
                new_fish.rect.y = new_fish.rect.height + 1.5 * new_fish.rect.height * row_index

                self.fishes.add(new_fish)

    def update_fishes(self):
        self.check_row_edges()
        self.fishes.update()

    def check_row_edges(self):
        for fish in self.fishes.sprites():
            if fish.check_fish_on_edges():
                self.change_row_direction()
                break

    def change_row_direction(self):
        for fish in self.fishes.sprites():
            fish.rect.y += self.settings.rows_drop
        self.settings.rows_direction *= -1

    def update_nets_number(self):
        self.check_net_limit()
        for net in self.nets.copy():
            if net.rect.bottom <= 0:
                self.nets.remove(net)
        collisions = pygame.sprite.groupcollide(self.nets, self.fishes, False, True)
        if collisions:
            self.settings.scores += 10
            self.score_instance.prep_score()
        if len(self.fishes) == 0:
            self.create_fishes_row()

    def fire_net(self):
        if self.settings.net_limit >= 0:
            net = Fishing_Net(self.settings, self.screen, self.ship)
            self.nets.add(net)
            self.settings.net_limit -= 1
            self.settings.net_width -= 2
        else:
            self.check_net_limit()

    def check_net_limit(self):
        if self.settings.net_limit < 1 and len(self.nets) <= 0:
            self.settings.game_active = False





