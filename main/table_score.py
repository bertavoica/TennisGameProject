import pygame, pygame.font
from menu import *

class Score():

    def __init__(self):
        self.current_player_score = 0
        self.current_enemy_score = 0
        self.games_player_score = 0
        self.games_enemy_score = 0
        self.sets_player_score = 0
        self.sets_enemy_score = 0
        self.advantage = False
        self.score_font = pygame.font.SysFont(None, 50)

    def upgrade_current(self):
        if self.current_player_scoreplayer_score < 40:
            self.current_player_score += 15
        elif self.current_player_score == 40:
            self.advantage = True

    def reinit_current(self):
        self.current_player_score = 0
        self.current_enemy_score = 0

    def upgrade_games(self):
        if self.games_player_score < 6:
            self.games_player_score += 1

    def reinit_games(self):
        reinit_current()
        self.games_player_score = 0
        self.games_player_score = 0

    def main():
    table_score = pygame.display.set_mode(100,50)
    table_score.fill((0, 0, 255))