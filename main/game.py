import pygame
import random
from constants import *

right = False
left = False


class Game:

    def __init__(self, screen):
        self.line = []
        self.screen = screen
        self.fillet = pygame.Rect(150, 225, 205, 5)

        self.game_started = False
        self.player_strike_left = False
        self.player_strike_right = False
        self.ball_speed = 0

        self.playerScore = 0
        self.botScore = 0
        self.bx = 0
        self.by = -110
        self.x = 150
        self.y = 300

        self.position_x = 0
        self.position_y = 0
        self.dimension_x = 24
        self.dimension_y = 24
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
            return
        if self.position_y - self.dimension_y < -10:
            self.game_started = False
            self.bx = 0
            self.by = -110
            self.x = 150
            self.y = 300
            self.playerScore += 1
        if self.position_y + self.dimension_y > HEIGHT_GAME:
            self.game_started = False
            self.bx = 0
            self.by = -110
            self.x = 150
            self.y = 300
            self.playerScore -= 1
        if self.position_x - self.dimension_x < -10:
            self.position_x = WIDTH_GAME / 2
            self.position_y = HEIGHT_GAME / 2
            self.playerScore += 1
        if self.position_x + self.dimension_x > WIDTH_GAME + 10:
            self.position_x = WIDTH_GAME / 2
            self.position_y = HEIGHT_GAME / 2
            self.botScore += 1

        self.position_x += self.velocity[0]
        self.position_y += self.velocity[1]
        print(str(self.velocity))
        #bot movement

        if self.position_x > self.bx + 175:
            self.bx += BOT_VELOCITY
        if self.position_x < self.bx + 175:
            self.bx -= BOT_VELOCITY

        self.collision_detection()

    def collision_detection(self):
        self.collision_of_ball()

    def collision_of_ball(self):
        # for player
        ball_center_x = self.position_x + HALF_BALL_SPRITE
        ball_center_y = self.position_y + HALF_BALL_SPRITE

        if ball_center_x + HALF_BALL_SPRITE > self.x + HALF_IMAGE_PLAYER_SPRITE_X - HALF_PLAYER_SPRITE and \
                ball_center_x - HALF_BALL_SPRITE < self.x + HALF_IMAGE_PLAYER_SPRITE_X + HALF_PLAYER_SPRITE and \
                ball_center_y - HALF_BALL_SPRITE < self.y + HALF_IMAGE_PLAYER_SPRITE_Y + HALF_PLAYER_SPRITE and \
                ball_center_y + HALF_BALL_SPRITE > self.y + HALF_IMAGE_PLAYER_SPRITE_Y - HALF_PLAYER_SPRITE:
            if self.player_strike_left:
                self.velocity = [-2 - random.randrange(0, int(self.ball_speed / 3) + 1),
                                 -7 + random.randrange(-1, 1) - self.ball_speed]
            else:
                self.velocity = [2 + random.randrange(0, int(self.ball_speed / 3) + 1),
                                 -7 + random.randrange(-1, 1) - self.ball_speed]
            self.ball_speed += 1

        if ball_center_x + HALF_BALL_SPRITE > self.bx + HALF_IMAGE_BOT_SPRITE_X - HALF_BOT_SPRITE and \
                ball_center_x - HALF_BALL_SPRITE < self.bx + HALF_IMAGE_BOT_SPRITE_X + HALF_BOT_SPRITE and \
                ball_center_y - HALF_BALL_SPRITE < self.by + HALF_IMAGE_BOT_SPRITE_Y + HALF_BOT_SPRITE and \
                ball_center_y + HALF_BALL_SPRITE > self.by + HALF_IMAGE_BOT_SPRITE_Y - HALF_BOT_SPRITE:
            self.ball_speed += 1
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
                    self.ball_speed = 0
                self.player_strike_left = True
                self.player_strike_right = False
                self.game_started = True
                self.player_profile = pygame.image.load("player_left.PNG")
                self.screen.blit(self.player_profile, (self.x, self.y))
            if keys[pygame.K_x]:
                if not self.game_started:
                    self.velocity = [2, -7 + random.randrange(-1, 1)]
                    self.ball_speed = 0
                self.player_strike_left = False
                self.player_strike_right = True
                self.game_started = True
                self.player_profile = pygame.image.load("player_right.PNG")
                self.screen.blit(self.player_profile, (self.x, self.y))
            if keys[pygame.K_LEFT] and self.position_x > VELOCITY:
                self.x -= VELOCITY
                self.player_profile = pygame.image.load("player_profile.PNG")
                self.screen.blit(self.player_profile, (self.x, self.y))

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

        self.screen.blit(self.player_profile, (self.x, self.y))
        self.screen.blit(self.bot, (self.bx, self.by))
        if self.game_started:
            self.screen.blit(self.ball, (self.position_x, self.position_y))
        pygame.display.update()


pygame.quit()
