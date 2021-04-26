# start menu window
import functools

import pygame, random, sys, pygame_menu, pybutton
from constants import *
from game import *
import pygame_widgets as pw

pygame.init()

GO_TO_GAME = False
text = ""


def start_the_game():
    global GO_TO_GAME
    print('clicked')
    GO_TO_GAME = True


def menu_game(screen):
    global GO_TO_GAME
    fps_cap = 30
    RUNNING = True
    clock = pygame.time.Clock()
    pygame.display.set_caption('PyGame Tennis Game!')
    background = pygame.image.load(
        r'C:\Users\berta\PycharmProjects\pythonProject\TennisGameProject\main\background.png')

    button_1 = pw.Button(
        screen, 100, 100, 100, 100, text='Start',
        fontSize=30, margin=20,
        inactiveColour=(255, 0, 0),
        pressedColour=(0, 255, 0), radius=10,
        onClick=start_the_game
    )

    button_2 = pw.Button(
        screen, 10, 10, 100, 100, text='Quit!',
        fontSize=30, margin=20,
        inactiveColour=(255, 0, 0),
        pressedColour=(0, 255, 0), radius=10,
        onClick=lambda: print('Click')
    )

    while RUNNING:
        events = pygame.event.get()
        clock.tick(fps_cap)
        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        action = ['Start', 'Quit!']

        for event in events:
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return FIRST_SCENE
                elif event.key == button_1.function():
                    return SECOND_SCENE
                pygame.display.flip()

        button_1.listen(events)
        button_1.draw()

        button_2.listen(events)
        button_2.draw()

        if GO_TO_GAME:
            print('go')
            GO_TO_GAME = False
            return SECOND_SCENE
        pygame.display.update()


def main():
    screen = pygame.display.set_mode(RESOLUTION)

    scene = FIRST_SCENE
    while True:
        if scene == FIRST_SCENE:
            scene = menu_game(screen)
        elif scene == SECOND_SCENE:
            scene = start_game(screen)


main()
