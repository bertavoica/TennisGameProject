# second window
import pygame
from constants import *
from components import *

right = False
left = False


class Game:
    def __init__(self, screen):
        self.line = []
        self.screen = screen
        self.fillet = pygame.Rect(150, 225, 205, 5)
        # object coordinates
        self.object_coordinate_x = 100
        self.object_coordinate_y = 100

        # object dimensions
        self.object_dimension_x = 15
        self.object_dimension_y = 15

        self.bx = 0
        self.by = -110
        self.x = 150
        self.y = 300

        self.player_profile = pygame.image.load("player_profile.PNG")
        self.bot = pygame.image.load("bot2.png")

    def start_game(self):
        pygame.display.set_caption("Start game!")
        pygame.draw.rect(self.screen, (0, 255, 0), (POINT_X, POINT_Y, WIDTH_GAME, HEIGHT_GAME))

    def run(self):
        RUN = True
        ball_object = Ball(WIDTH_GAME/2, HEIGHT_GAME/2, VELOCITY, VELOCITY, WIDTH_GAME/2, HEIGHT_GAME/2, self.screen)
        while RUN:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.object_coordinate_x > VELOCITY:
                self.x -= VELOCITY
                self.bx = ball_object.position_x
                if keys[pygame.K_SPACE]:
                    self.player_profile = pygame.image.load("player_left.PNG")
                    self.screen.blit(self.player_profile, (self.x, self.y))
                else:
                    self.player_profile = pygame.image.load("player_profile.PNG")
                    self.screen.blit(self.player_profile, (self.x, self.y))

            if keys[pygame.K_UP] and self.object_coordinate_y > VELOCITY:
                self.y -= VELOCITY
                self.by += ball_object.position_y
            if keys[pygame.K_DOWN]:
                self.y += VELOCITY
                self.by -= ball_object.position_y
            if keys[pygame.K_RIGHT]:
                self.x += VELOCITY
                self.bx -= ball_object.position_x
                if keys[pygame.K_SPACE]:
                    self.player_profile = pygame.image.load("player_right.PNG")
                    self.screen.blit(self.player_profile, (self.x, self.y))
                else:
                    self.player_profile = pygame.image.load("player_profile.PNG")
                    self.screen.blit(self.player_profile, (self.x, self.y))
            self.screen.fill((0, 255, 0))
            self.draw()

    def draw(self):
        self.line.append(pygame.Rect(100, 50, 5, 400))
        self.line.append(pygame.Rect(400, 50, 5, 400))
        self.line.append(pygame.Rect(100, 50, 300, 5))
        self.line.append(pygame.Rect(100, 450, 305, 5))
        self.line.append(pygame.Rect(150, 50, 5, 400))
        self.line.append(pygame.Rect(350, 50, 5, 400))
        self.line.append(pygame.Rect(150, 160, 200, 5))
        self.line.append(pygame.Rect(150, 290, 200, 5))
        self.line.append(pygame.Rect(250, 160, 5, 130))
        pygame.draw.rect(self.screen, (255, 255, 255), self.line[0])
        pygame.draw.rect(self.screen, (255, 255, 255), self.line[1])
        pygame.draw.rect(self.screen, (255, 255, 255), self.line[2])
        pygame.draw.rect(self.screen, (255, 255, 255), self.line[3])
        pygame.draw.rect(self.screen, (255, 255, 255), self.line[4])
        pygame.draw.rect(self.screen, (255, 255, 255), self.line[5])
        pygame.draw.rect(self.screen, (255, 255, 255), self.line[6])
        pygame.draw.rect(self.screen, (255, 255, 255), self.line[7])
        pygame.draw.rect(self.screen, (255, 255, 255), self.line[8])
        pygame.draw.rect(self.screen, BLACK, self.fillet)
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.object_coordinate_x, self.object_coordinate_y, self.object_dimension_x,
                          self.object_dimension_y))
        self.screen.blit(self.player_profile, (self.x, self.y))
        self.screen.blit(self.bot, (self.bx, self.by))
        pygame.display.update()


pygame.quit()
