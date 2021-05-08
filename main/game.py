# second window
import pygame
import random
from constants import *

right = False
left = False


class Game:

    # game = Game(screen)
    # self.ball = Ball(self, [WIDTH_GAME / 2, HEIGHT_GAME / 2], [BALL_RADIUS, BALL_RADIUS], [0, 0], screen)

    def __init__(self, screen):
        self.line = []
        self.screen = screen
        self.fillet = pygame.Rect(150, 225, 205, 5)
        # object coordinates
        # self.object_coordinate_x = 100
        # self.object_coordinate_y = 100

        # object dimensions
        # self.object_dimension_x = 60
        # self.object_dimension_y = 15

        self.game_started = False

        self.playerScore = 0
        self.botScore = 0
        self.bx = 0
        self.by = -110
        self.x = 150
        self.y = 300

        self.position_x = 0
        self.position_y = 0
        self.dimension_x = 2
        self.dimension_y = 2
        # self.velocity = [5 + random.randrange(-1, 1), 5 + random.randrange(-1, 1)]
        self.player_profile = pygame.image.load("player_profile.PNG")
        self.bot = pygame.image.load("bot2.png")
        self.ball = pygame.image.load("ball.png")

    def start_game(self):
        pygame.display.set_caption("Start game!")
        pygame.draw.rect(self.screen, (0, 255, 0), (POINT_X, POINT_Y, WIDTH_GAME, HEIGHT_GAME))

    def update(self):
        if not self.game_started:
            self.position_x = self.x + 175
            self.position_y = self.y + 147 - 50
            # print(str(self.position_x))
            # print(str(self.position_y))
            return
        # self.position_x = int(self.position_x)
        # self.position_y = int(self.position_y)
        # self.velocity = [0, 0]
        # print(str(self.position_x))
        # if self.position_x - self.dimension_x < -10:
        #     self.velocity[0] *= -1
        # if self.position_x + self.dimension_x > WIDTH_GAME + 10:
        #     self.velocity[0] *= -1

        # could be simplified by telling that if the ball is not hit on the other half of the field, it's a point for
        # the opponent
        if self.position_y - self.dimension_y < -10:
            self.game_started = False
            self.bx = 0
            self.by = -110
            self.x = 150
            self.y = 300
            # self.game.ball = Ball(self.game, [WIDTH_GAME // 2, HEIGHT_GAME // 2], [BALL_RADIUS, BALL_RADIUS])
            self.playerScore += 1
        if self.position_y + self.dimension_y > HEIGHT_GAME:
            self.game_started = False
            self.bx = 0
            self.by = -110
            self.x = 150
            self.y = 300
            # self.game.ball = Ball(self.game, [WIDTH_GAME // 2, HEIGHT_GAME // 2], [BALL_RADIUS, BALL_RADIUS])
            self.playerScore -= 1
        if self.position_x - self.dimension_x < -10:
            # self.game.ball = Ball(self.game, [WIDTH_GAME // 2, HEIGHT_GAME // 2], [BALL_RADIUS, BALL_RADIUS])
            self.position_x = WIDTH_GAME / 2
            self.position_y = HEIGHT_GAME / 2
            self.playerScore += 1
        if self.position_x + self.dimension_x > WIDTH_GAME + 10:
            # self.game.ball = Ball(self.game, [WIDTH_GAME // 2, HEIGHT_GAME // 2], [BALL_RADIUS, BALL_RADIUS])
            self.position_x = WIDTH_GAME / 2
            self.position_y = HEIGHT_GAME / 2
            self.botScore += 1
        # TODO, WHEN THE BALL TOUCHES THE FIELD OF THE PLAYER THAT HIT IT IN THAT MOMENT. IT IS A POINT FOR THE OTHER
        #  PLAYER
        self.position_x += self.velocity[0]
        self.position_y += self.velocity[1]
        print(str(self.velocity))

        if self.position_x > self.bx + 175:
            self.bx += BOT_VELOCITY
        if self.position_x < self.bx + 175:
            self.bx -= BOT_VELOCITY

        self.collision_detection()


    def collision_detection(self):
        self.collision_of_ball()
            # self.on_collision()

    # def on_collision(self):
    #     self.velocity[0] *= -1.4

    def collision_of_ball(self):
        # for player
        if self.position_x - (self.dimension_x + 10) / 2 < self.x + 175 + (self.x + 175 + 10) / 2 and \
                self.position_x + (self.dimension_x + 10) / 2 > self.x + 175 - (self.x + 175 + 10) / 2 and \
                self.position_y - self.dimension_y / 2 < self.y + 147 + (self.y + 147) / 2 and \
                self.position_y + self.dimension_y / 2 > self.y + 147 - (self.y + 147) / 2:
            self.velocity[1] *= -1
        if self.position_x - (self.dimension_x + 10) / 2 < self.bx + 175 + (self.bx + 175 + 10) / 2 and \
                self.position_x + (self.dimension_x + 10) / 2 > self.bx + 175 - (self.bx + 175 + 10) / 2 and \
                self.position_y - self.dimension_y / 2 < self.by + 147 + (self.by + 147) / 2 and \
                self.position_y + self.dimension_y / 2 > self.by + 147 - (self.by + 147) / 2:
            self.velocity[1] *= -1

    def run(self):
        RUN = True
        self.game_started = False
        while RUN:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
            keys = pygame.key.get_pressed()
            self.screen.blit(self.ball, (self.position_x, self.position_y))
            if keys[pygame.K_z]:
                if not self.game_started:
                    self.velocity = [-2, -7 + random.randrange(-1, 1)]
                self.game_started = True
                self.player_profile = pygame.image.load("player_left.PNG")
                self.screen.blit(self.player_profile, (self.x, self.y))
            if keys[pygame.K_x]:
                if not self.game_started:
                    self.velocity = [2, -7 + random.randrange(-1, 1)]
                self.game_started = True
                self.player_profile = pygame.image.load("player_right.PNG")
                self.screen.blit(self.player_profile, (self.x, self.y))
            if keys[pygame.K_LEFT] and self.position_x > VELOCITY:
                self.x -= VELOCITY
                self.player_profile = pygame.image.load("player_profile.PNG")
                self.screen.blit(self.player_profile, (self.x, self.y))
                # if keys[pygame.K_SPACE]:
                #     self.player_profile = pygame.image.load("player_left.PNG")
                #     self.screen.blit(self.player_profile, (self.x, self.y))
                # else:
                #     self.player_profile = pygame.image.load("player_profile.PNG")
                #     self.screen.blit(self.player_profile, (self.x, self.y))

            if keys[pygame.K_UP] and self.position_y > VELOCITY:
                self.y -= VELOCITY
                self.player_profile = pygame.image.load("player_profile.PNG")
                self.screen.blit(self.player_profile, (self.x, self.y))
            if keys[pygame.K_DOWN]:
                self.y += VELOCITY
                self.player_profile = pygame.image.load("player_profile.PNG")
                self.screen.blit(self.player_profile, (self.x, self.y))
            if keys[pygame.K_RIGHT]:
                self.x += VELOCITY
                self.player_profile = pygame.image.load("player_profile.PNG")
                self.screen.blit(self.player_profile, (self.x, self.y))
                # if keys[pygame.K_SPACE]:
                #     self.player_profile = pygame.image.load("player_right.PNG")
                #     self.screen.blit(self.player_profile, (self.x, self.y))
                # else:
                #     self.player_profile = pygame.image.load("player_profile.PNG")
                #     self.screen.blit(self.player_profile, (self.x, self.y))
            self.screen.fill((0, 255, 0))
            self.update()
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
        # pygame.draw.rect(self.screen, (255, 0, 0),
        #                  (self.object_coordinate_x, self.object_coordinate_y, self.object_dimension_x,
        # self.object_dimension_y))
        self.screen.blit(self.player_profile, (self.x, self.y))
        self.screen.blit(self.bot, (self.bx, self.by))
        if self.game_started:
            # self.screen.blit(self.ball, (self.x + 175, self.y + 147))
            self.screen.blit(self.ball, (self.position_x, self.position_y))
        # pygame.draw.circle(self.screen, WHITE, (self.position_x, self.position_y), BALL_RADIUS)
        pygame.display.update()


pygame.quit()
