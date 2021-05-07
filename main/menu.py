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
        self.text = ''
        self.font_title = pygame.font.SysFont(None, 65)
        self.txt_surface = self.font.render(self.text, True, BLACK)
        self.width = max(200, self.txt_surface.get_width() + 10)
        self.font_intro = pygame.font.SysFont(None, 30)
        self.text_intro = self.font_intro.render("Enter your name:", True, BLACK)
        self.text_title = self.font_title.render("Tennis Game!", True, BLACK)
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(
            r'C:\Users\HP\Desktop\proiect_python\TennisGameProject\main\background.png')
        self.fps_cap = 30
        self.input_box = py.Rect(10, 30, 100, 100)
        self.color_inactive = WHITE
        self.color_active = RED
        self.color = self.color_inactive
        self.user_list = []
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
        pygame.display.set_caption('PyGame Tennis Game!')
        py.draw.rect(self.screen, self.color, self.input_box, 2)

    def run_menu(self):
        global RUNNING, GO_TO_GAME
        active = False

        while RUNNING:
            events = pygame.event.get()
            self.clock.tick(self.fps_cap)
            self.screen.fill(WHITE)
            self.screen.blit(self.background, (0, 0))

            for event in events:
                if event.type == pygame.QUIT:
                    RUNNING = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    self.color = self.color_active if active else self.color_inactive
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        return FIRST_SCENE
                    elif event.key == self.button_1.function():
                        return SECOND_SCENE
                    if active:
                        if event.key == py.K_RETURN:
                            print(self.text)
                            self.text = ''
                        elif event.key == py.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode

                self.button_1.listen(events)
                self.button_2.listen(events)

            if GO_TO_GAME:
                print('go')
                GO_TO_GAME = False
                return SECOND_SCENE

            self.draw()

    def draw(self):
        global GO_TO_GAME
        self.input_box.w = self.width
        self.button_1.draw()
        self.button_2.draw()
        self.text = ''
        self.screen.blit(self.text_title, self.text_title.get_rect(center=self.screen.get_rect().center))
        self.screen.blit(self.text_intro, self.text_intro.get_rect(center=(100, 20)))
        self.screen.blit(self.txt_surface, (self.input_box.x + 5, self.input_box.y + 5))

        pygame.display.update()

        # solved flickering by removing the flip function and add it to the bottom
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
            print("ccc")
            game_object.start_game()
            game_object.run()


main()
