# start menu window
import pygame as py
from game import Game
import sys
import pygame_widgets as pw
from constants import *

py.init()

GO_TO_GAME = False
RUNNING = True


def quit_the_game():
    global RUNNING
    print('quit game')
    sys.exit()


def start_the_game():
    global GO_TO_GAME
    print('clicked')
    GO_TO_GAME = True


class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.font = py.font.Font(None, 32)
        self.font_title = pygame.font.SysFont(None, 65)
        self.text_title = self.font_title.render("Tennis Game!", True, BLACK)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(
            r'C:\Users\berta\PycharmProjects\pythonProject\TennisGameProjectSecondTry\main\background.png')
        self.fps_cap = 30
        self.button_1 = pw.Button(
            self.screen, WIDTH_MENU / 2 - 270, 500, 100, 100, text='Start',
            fontSize=30, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=10,
            onClick=start_the_game
        )
        self.button_2 = pw.Button(
            self.screen, WIDTH_MENU / 2 + 270, 500, 100, 100, text='Quit!',
            fontSize=30, margin=20,
            inactiveColour=(255, 0, 0),
            pressedColour=(0, 255, 0), radius=10,
            onClick=quit_the_game
        )

    def start_menu(self):
        self.draw()
        pygame.display.set_caption('PyGame Tennis Game!')

    def run_menu(self):
        global RUNNING, GO_TO_GAME

        while RUNNING:
            events = pygame.event.get()
            self.clock.tick(self.fps_cap)
            self.screen.fill(WHITE)
            self.screen.blit(self.background, (0, 0))

            for event in events:
                if event.type == pygame.QUIT:
                    RUNNING = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            return FIRST_SCENE
                        elif event.key == self.button_1.function():
                            return SECOND_SCENE

                self.button_1.listen(events)
                self.button_2.listen(events)

            if GO_TO_GAME:
                print('go')
                GO_TO_GAME = False
                return SECOND_SCENE

            self.draw()

    def draw(self):
        global GO_TO_GAME
        self.button_1.draw()
        self.button_2.draw()
        self.screen.blit(self.text_title, self.text_title.get_rect(center=self.screen.get_rect().center))

        pygame.display.update()

        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)

    scene = FIRST_SCENE
    game_object = Game(screen)
    menu_object = Menu(screen)
    while True:
        if scene == FIRST_SCENE:
            menu_object.start_menu()
            scene = menu_object.run_menu()
        elif scene == SECOND_SCENE:
            game_object.start_game()
            game_object.run()


main()
