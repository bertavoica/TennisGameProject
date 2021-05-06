from constants import *
import random
from game import *


class Ball(Game):
    def __init__(self, game, position, dimensions, velocity, screen):
        super().__init__(screen)
        velocity = [0, 0]
        while velocity[0] == 0 or velocity[1] == 0:
            velocity = [random.randrange(-1, 1), random.randrange(-1, 1)]
        self.position = position
        self.dimensions = dimensions
        self.game = game
        self.velocity = velocity

    def draw(self):
        pygame.draw.circle(self.screen.window, GREEN, self.position, BALL_RADIUS)

    def update(self):
        self.position[0] = int(self.velocity[0])
        self.position[1] = int(self.velocity[1])

        if self.position[0] - self.dimensions[0] < -10:
            self.velocity[0] *= -1
        if self.position[0] + self.dimensions[0] > WIDTH_GAME + 10:
            self.velocity[0] *= -1

        # could be simplified by telling that if the ball is not hit on the other half of the field, it's a point for
        # the opponent
        if self.position[1] - self.dimensions[1] < -10:
            self.game.ball = Ball(self.game, [WIDTH_GAME // 2, HEIGHT_GAME // 2], [BALL_RADIUS, BALL_RADIUS])
            self.game.playerScore += 1
        if self.position[0] + self.dimensions[0] > HEIGHT_GAME + 10:
            self.game.ball = Ball(self.game, [WIDTH_GAME // 2, HEIGHT_GAME // 2], [BALL_RADIUS, BALL_RADIUS])
            self.game.botScore += 1
        # TODO, WHEN THE BALL TOUCHES THE FIELD OF THE PLAYER THAT HIT IT IN THAT MOMENT. IT IS A POINT FOR THE OTHER
        #  PLAYER
    def onCollision(self, other):
        self.velocity[0] *= -1.4

    def collisionOfBall(self, game):
        #for player
        if self.position[0] - (self.dimensions[0] + 10) / 2 < game.object_coordinate_x + (
                game.object_dimension_x + 10) / 2 and \
                self.position[0] + (self.dimensions[0] + 10) / 2 > game.object_coordinate_x - (
                game.object_dimension_x + 10) / 2 and \
                self.position[1] - self.dimensions[1] / 2 < game.object_coordinate_y + \
                game.object_dimension_y / 2 and \
                self.position[1] + self.dimensions[1] / 2 > game.object_coordinate_y - \
                game.object_dimension_y / 2:
            self.velocity[0] *= -1
        #TODO FOR BOT
