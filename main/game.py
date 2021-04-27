# second window
import pygame, random, sys, pygame_menu, pybutton
from constants import *


def start_game(screen):
    fps_cap = 30
    clock = pygame.time.Clock()
    pygame.display.set_caption('Start game!')
    events = pygame.event.get()
    game_background = pygame.image.load(
        r'C:\Users\berta\PycharmProjects\pythonProject\TennisGameProject\main\tennis_court.png').convert()

    picture = pygame.transform.scale(game_background, (720, 720))

    while True:
        clock.tick(fps_cap)
        screen.fill(WHITE)
        screen.blit(picture, (0, 0, WIDTH, HEIGHT))
        for event in events:
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    return FIRST_SCENE
                elif event.key == pygame.K_b:
                    return SECOND_SCENE

        pygame.display.update()
