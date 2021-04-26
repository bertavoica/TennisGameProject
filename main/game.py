# second window
import pygame, random, sys, pygame_menu, pybutton
from constants import *


def start_game(screen):
    fps_cap = 30
    # items = ['choose a player', 'choose a pallete', 'choose a team']
    clock = pygame.time.Clock()
    pygame.display.set_caption('Start game!')
    events = pygame.event.get()

    while True:
        clock.tick(fps_cap)

        for event in events:
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    return FIRST_SCENE
                elif event.key == pygame.K_b:
                    return SECOND_SCENE

        # print('Choose:', *items)

        screen.fill((0, 0, 255))
        pygame.display.update()
