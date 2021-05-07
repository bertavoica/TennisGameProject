# second window
import pygame
import random
import time
from constants import *
from tqdm import *
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

        self.playerScore = 0
        self.botScore = 0
        self.bx = 0
        self.by = -110
        self.x = 150
        self.y = 300
        #loading bar

        self.barPos = (30, 250)
        self.barSize = (20, 200)
        self.borderColor = (0, 0, 0)
        self.barColor = RED
        self.count = 0

        self.position_x = WIDTH_GAME / 2
        self.position_y = HEIGHT_GAME / 2
        self.dimension_x = 2
        self.dimension_y = 2
        self.velocity = [0, 0]
        self.count = 0
        while self.velocity[0] == 0 or self.velocity[1] == 0:
            # print("aaaa")
            self.velocity = [random.randrange(-1, 1), random.randrange(-1, 1)]
        self.player_profile = pygame.image.load("player_profile.PNG")
        self.bot = pygame.image.load("bot2.png")

    def start_game(self):
        pygame.display.set_caption("Start game!")
        pygame.draw.rect(self.screen, (0, 255, 0), (POINT_X, POINT_Y, WIDTH_GAME, HEIGHT_GAME))

    def update(self):
        self.position_x = int(self.position_x)
        self.position_y = int(self.position_y)

        if self.position_x - self.dimension_x < -10:
            self.velocity[0] *= -1
        if self.position_x + self.dimension_x > WIDTH_GAME + 10:
            self.velocity[0] *= -1

        # could be simplified by telling that if the ball is not hit on the other half of the field, it's a point for
        # the opponent
        if self.position_y - self.dimension_y < -10:
            # self.game.ball = Ball(self.game, [WIDTH_GAME // 2, HEIGHT_GAME // 2], [BALL_RADIUS, BALL_RADIUS])
            self.position_x = WIDTH_GAME / 2
            self.position_y = HEIGHT_GAME / 2
            self.playerScore += 1
        if self.position_x + self.dimension_x > HEIGHT_GAME + 10:
            # self.game.ball = Ball(self.game, [WIDTH_GAME // 2, HEIGHT_GAME // 2], [BALL_RADIUS, BALL_RADIUS])
            self.position_x = WIDTH_GAME / 2
            self.position_y = HEIGHT_GAME / 2
            self.botScore += 1
        # TODO, WHEN THE BALL TOUCHES THE FIELD OF THE PLAYER THAT HIT IT IN THAT MOMENT. IT IS A POINT FOR THE OTHER
        #  PLAYER
        self.collision_detection()

    def collision_detection(self):
        if self.collision_of_ball():
            self.on_collision()

    def on_collision(self):
        self.velocity[0] *= -1.4

    def collision_of_ball(self):
        # for player
        if self.position_x - (self.dimension_x + 10) / 2 < self.object_coordinate_x + (
                self.object_dimension_x + 10) / 2 and \
                self.position_x + (self.dimension_x + 10) / 2 > self.object_coordinate_x - (
                self.object_dimension_x + 10) / 2 and \
                self.position_y - self.dimension_y / 2 < self.object_coordinate_y + \
                self.object_dimension_y / 2 and \
                self.position_y + self.dimension_y / 2 > self.object_coordinate_y - \
                self.object_dimension_y / 2:
            self.velocity[0] *= -1
        # TODO FOR BOT

    def run(self):
        RUN = True
        while RUN:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.count += 0.2
            if self.count > 13.799999999999982:
                self.count = 13.799999999999983
                self.count = 13.799999999999983
            if keys[pygame.K_LEFT] and self.object_coordinate_x > VELOCITY:
                self.x -= VELOCITY
                if keys[pygame.K_SPACE]:
                    self.player_profile = pygame.image.load("player_left.PNG")
                    self.screen.blit(self.player_profile, (self.x, self.y))
                else:
                    self.player_profile = pygame.image.load("player_profile.PNG")
                    self.screen.blit(self.player_profile, (self.x, self.y))

            if keys[pygame.K_UP] and self.object_coordinate_y > VELOCITY:
                self.y -= VELOCITY

            if keys[pygame.K_DOWN]:
                self.y += VELOCITY
            if keys[pygame.K_RIGHT]:
                self.x += VELOCITY
                if keys[pygame.K_SPACE]:
                    self.player_profile = pygame.image.load("player_right.PNG")
                    self.screen.blit(self.player_profile, (self.x, self.y))
                else:
                    self.player_profile = pygame.image.load("player_profile.PNG")
                    self.screen.blit(self.player_profile, (self.x, self.y))
            self.screen.fill((0, 255, 0))
            self.update()
            self.draw()

    def DrawBar(self, pos, size, borderC, barC, progress):

        pygame.draw.rect(self.screen, borderC, (*pos, *size), 1)
        innerPos = (pos[0] + 3, pos[1] + 3)
        innerSize = ((size[0] - 6), (size[0] - 6) * progress)
        print(progress)
        pygame.draw.rect(self.screen, barC, (*innerPos, *innerSize))

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
        self.DrawBar(self.barPos, self.barSize, self.borderColor, self.barColor, self.count)
        self.screen.blit(self.player_profile, (self.x, self.y))
        self.screen.blit(self.bot, (self.bx, self.by))
        pygame.draw.circle(self.screen, RED, (self.position_x, self.position_y), BALL_RADIUS)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(700, 700, 20, 20))
        pygame.display.update()

pygame.quit()
