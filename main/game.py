import pygame
import random
from constants import *

right = False
left = False
pygame.mixer.init()


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

        # loading bar
        self.barPos = (30, 250)
        self.barSize = (20, 200)
        self.borderColor = (0, 0, 0)
        self.barColor = RED
        self.count = 0

        self.position_x = 0
        self.position_y = 0
        self.dimension_x = 24
        self.dimension_y = 24
        self.player_profile = pygame.image.load("player_profile.PNG")
        self.bot = pygame.image.load("bot2.png")
        self.ball = pygame.image.load("ball.png")
        self.my_font = pygame.font.SysFont(None, 40)

    def start_game(self):
        pygame.display.set_caption("Start game!")
        pygame.draw.rect(self.screen, (0, 255, 0), (POINT_X, POINT_Y, WIDTH_GAME, HEIGHT_GAME))

    def increase_player_score(self):
        if self.playerScore == 30:
            self.playerScore += 10
        else:
            self.playerScore += 15

    def increase_bot_score(self):
        if self.botScore == 30:
            self.botScore += 10
        else:
            self.botScore += 15

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
            self.increase_player_score()
            self.count = 0
            pygame.mixer.music.load('mixkit-audience-light-applause-354.wav')
            pygame.mixer.music.play()
        if self.position_y + self.dimension_y > HEIGHT_GAME:
            self.game_started = False
            self.bx = 0
            self.by = -110
            self.x = 150
            self.y = 300
            self.increase_bot_score()
            self.count = 0
            pygame.mixer.music.load('mixkit-audience-light-applause-354.wav')
            pygame.mixer.music.play()
        if self.position_x - self.dimension_x < -10:
            self.game_started = False
            self.bx = 0
            self.by = -110
            self.x = 150
            self.y = 300
            if self.velocity[1] < 0:
                self.increase_bot_score()
            else:
                self.increase_player_score()
            self.count = 0
            pygame.mixer.music.load('mixkit-audience-light-applause-354.wav')
            pygame.mixer.music.play()
        if self.position_x + self.dimension_x > WIDTH_GAME + 10:
            self.game_started = False
            self.bx = 0
            self.by = -110
            self.x = 150
            self.y = 300
            if self.velocity[1] < 0:
                self.increase_bot_score()
            else:
                self.increase_player_score()
            self.count = 0

            pygame.mixer.music.load('mixkit-audience-light-applause-354.wav')
            pygame.mixer.music.play()

        self.position_x += self.velocity[0]
        self.position_y += self.velocity[1]
        print(str(self.velocity))

        if self.position_x > self.bx + 175:
            self.bx += BOT_VELOCITY
        if self.position_x < self.bx + 175:
            self.bx -= BOT_VELOCITY
        print(self.playerScore)
        self.collision_detection()

    def collision_detection(self):
        self.collision_of_ball()

    def collision_of_ball(self):

        ball_center_x = self.position_x + HALF_BALL_SPRITE
        ball_center_y = self.position_y + HALF_BALL_SPRITE

        if ball_center_x + HALF_BALL_SPRITE > self.x + HALF_IMAGE_PLAYER_SPRITE_X - HALF_PLAYER_SPRITE and \
                ball_center_x - HALF_BALL_SPRITE < self.x + HALF_IMAGE_PLAYER_SPRITE_X + HALF_PLAYER_SPRITE and \
                ball_center_y - HALF_BALL_SPRITE < self.y + HALF_IMAGE_PLAYER_SPRITE_Y + HALF_PLAYER_SPRITE and \
                ball_center_y + HALF_BALL_SPRITE > self.y + HALF_IMAGE_PLAYER_SPRITE_Y - HALF_PLAYER_SPRITE:
            pygame.mixer.music.load('3dm_bik_ball.wav')
            pygame.mixer.music.play()
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
            pygame.mixer.music.load('3dm_bik_ball.wav')
            pygame.mixer.music.play()
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
            if keys[pygame.K_SPACE]:
                self.count += 1
            if self.count > 13.99999999999999:
                self.count = 0
            self.screen.blit(self.ball, (self.position_x, self.position_y))
            if keys[pygame.K_z]:
                if not self.game_started:
                    self.velocity = [-2, -7 + random.randrange(-1, 1)]
                    self.ball_speed = self.count
                self.player_strike_left = True
                self.player_strike_right = False
                self.game_started = True
                # reset score when one of the players won
                if self.playerScore == 40 or self.botScore == 40:
                    self.playerScore = 0
                    self.botScore = 0
            if keys[pygame.K_x]:
                if not self.game_started:
                    self.velocity = [2, -7 + random.randrange(-1, 1)]
                    self.ball_speed = self.count
                self.player_strike_left = False
                self.player_strike_right = True
                self.game_started = True
                if self.playerScore == 40 or self.botScore == 40:
                    self.playerScore = 0
                    self.botScore = 0
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
        self.DrawBar(self.barPos, self.barSize, self.borderColor, self.barColor, self.count)
        self.screen.blit(self.player_profile, (self.x, self.y))
        self.screen.blit(self.bot, (self.bx, self.by))
        self.score_text_player = self.my_font.render("Player Score = " + str(self.playerScore), True, (0, 0, 0))
        self.screen.blit(self.score_text_player, (10, 500))
        self.score_text_bot = self.my_font.render("Bot Score = " + str(self.botScore), True, (0, 0, 0))
        self.screen.blit(self.score_text_bot, (10, 540))

        if self.playerScore == 40:
            self.score_text_player_end = self.my_font.render("Winner: Player!", True, (0, 0, 0))
            self.screen.blit(self.score_text_player_end, (450, 200))
        if self.botScore == 40:
            self.score_text_player_end = self.my_font.render("Winner: Bot!", True, (0, 0, 0))
            self.screen.blit(self.score_text_player_end, (450, 200))

        if self.game_started:
            self.screen.blit(self.ball, (self.position_x, self.position_y))
        pygame.display.update()


pygame.quit()
