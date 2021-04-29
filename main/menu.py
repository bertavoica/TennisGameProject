# start menu window
import pygame as py
from game import *
import sys
import pygame_widgets as pw

pygame.init()

GO_TO_GAME = False
RUNNING = True


def start_the_game():
    global GO_TO_GAME
    print('clicked')
    GO_TO_GAME = True


def quit_the_game():
    global RUNNING
    print('quit game')
    sys.exit()


def menu_game(screen):
    global GO_TO_GAME, RUNNING
    text = ''
    fps_cap = 30
    clock = pygame.time.Clock()

    # window title
    pygame.display.set_caption('PyGame Tennis Game!')

    # background image
    background = pygame.image.load(r'C:\Users\Mircea\PycharmProjects\TennisGameProject\main\background.png')

    # input username
    input_box = py.Rect(10, 30, 100, 100)
    active = False
    font = py.font.Font(None, 32)
    color_inactive = WHITE
    color_active = RED
    color = color_inactive

    # screen title
    font_title = pygame.font.SysFont(None, 65)
    text_title = font_title.render("Tennis Game!", True, BLACK)

    # text input intro
    font_intro = pygame.font.SysFont(None, 30)
    text_intro = font_intro.render("Enter your name:", True, BLACK)

    # define a list what lately will append the username
    user_list = []

    button_1 = pw.Button(
        screen, WIDTH / 2 - 270, 500, 100, 100, text='Start',
        fontSize=30, margin=20,
        inactiveColour=(255, 0, 0),
        pressedColour=(0, 255, 0), radius=10,
        onClick=start_the_game
    )

    button_2 = pw.Button(
        screen, WIDTH / 2 + 270, 500, 100, 100, text='Quit!',
        fontSize=30, margin=20,
        inactiveColour=(255, 0, 0),
        pressedColour=(0, 255, 0), radius=10,
        onClick=quit_the_game
    )

    while RUNNING:
        events = pygame.event.get()
        clock.tick(fps_cap)
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        for event in events:
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    return FIRST_SCENE
                elif event.key == button_1.function():
                    return SECOND_SCENE
                if active:
                    if event.key == py.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == py.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        button_1.listen(events)
        button_1.draw()

        button_2.listen(events)
        button_2.draw()

        # positioning texts
        screen.blit(text_title, text_title.get_rect(center=screen.get_rect().center))

        screen.blit(text_intro, text_intro.get_rect(center=(100, 20)))

        # resize box if the text is too big or long
        txt_surface = font.render(text, True, BLACK)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        py.draw.rect(screen, color, input_box, 2)

        # saving username
        user_list.append(text)
        user_set = set(user_list)

        if GO_TO_GAME:
            print('go')
            GO_TO_GAME = False
            return SECOND_SCENE

        pygame.display.update()

        # solved flickering by removing the flip function and add it to the bottom
        pygame.display.flip()


def main():
    screen = pygame.display.set_mode(RESOLUTION)

    scene = FIRST_SCENE
    while True:
        if scene == FIRST_SCENE:
            scene = menu_game(screen)
        elif scene == SECOND_SCENE:
            scene = start_game(screen)


main()