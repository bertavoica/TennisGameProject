# second window
import pygame
#from menu import *
from constants import *
right=False
left=False


def start_game(screen):
    pygame.display.set_caption("Joc de tenis")
    line1 = pygame.Rect(100, 50, 5, 400)
    line2 = pygame.Rect(400, 50, 5, 400)
    line3 = pygame.Rect(100, 50, 300, 5)
    line4 = pygame.Rect(100, 450, 305, 5)
    line5 = pygame.Rect(150, 50, 5, 400)
    line6 = pygame.Rect(350, 50, 5, 400)
    line7 = pygame.Rect(150, 160, 200, 5)
    fillet = pygame.Rect(150, 225, 205, 5)
    line8 = pygame.Rect(150, 290, 200, 5)
    line9 = pygame.Rect(250, 160, 5, 130)
    imagine = pygame.image.load("poza_proba1.png")
    bot_inamic=pygame.image.load("bot2.png")
    # matrix dimensions that shows the positions for a point in our plan
    point_x = 0
    point_y = 0.1
    bx=0
    by=-110
    width = 800
    height = 800
    x=150
    y=300
    velocity = 5

    # object coordinates
    object_coordinate_x = 100
    object_coordinate_y = 100

    # object dimenstions
    object_dimension_x = 15
    object_dimension_y = 15

    pygame.draw.rect(screen, (0, 255, 0), (point_x, point_y, width, height))
    #background = pygame.image.load(r'C:\Users\Mircea\PycharmProjects\TennisGameProject\main\abc.png')
    run = True
    while run:
        pygame.time.delay(100)
     #   screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and object_coordinate_x > velocity:
            x -= velocity
            left = True
            if left==True and keys[pygame.K_SPACE]:
                imagine=pygame.image.load("lovitura_st.PNG")
                screen.blit(imagine,(x,y))
            else:
                imagine=pygame.image.load("poza_proba1.PNG")
                screen.blit(imagine,(x,y))
        if keys[pygame.K_UP] and object_coordinate_y > velocity:
            y -= velocity

        if keys[pygame.K_DOWN] :
            y += velocity
        if keys[pygame.K_RIGHT] :
            x += velocity
            right = True
            if right == True and keys[pygame.K_SPACE]:
                imagine = pygame.image.load("poza_lovit_dr.PNG")
                screen.blit(imagine, (x, y))
                right = False
            else:
                imagine = pygame.image.load("poza_proba1.PNG")
                screen.blit(imagine, (x, y))
                right = False
        screen.fill((0, 255, 0))




        pygame.draw.rect(screen, (255, 255, 255), line1)
        pygame.draw.rect(screen, (255, 255, 255), line2)
        pygame.draw.rect(screen, (255, 255, 255), line3)
        pygame.draw.rect(screen, (255, 255, 255), line4)
        pygame.draw.rect(screen, (255, 255, 255), line5)
        pygame.draw.rect(screen, (255, 255, 255), line6)
        pygame.draw.rect(screen, (255, 255, 255), line7)
        pygame.draw.rect(screen, (255, 255, 255), line8)
        pygame.draw.rect(screen, (255, 255, 255), line9)
        pygame.draw.rect(screen, BLACK, fillet)
        pygame.draw.rect(screen, (255, 0, 0),(object_coordinate_x, object_coordinate_y, object_dimension_x, object_dimension_y))
        screen.blit(imagine, (x, y))
        screen.blit(bot_inamic,(bx,by))
        pygame.display.update()
pygame.quit()