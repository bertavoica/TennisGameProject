from constants import *
import random


class Ball:

    def __init__(self, position_x, position_y, velocity_x, velocity_y, dimensions_x, dimensions_y, screen):
        while velocity_x == 0 or velocity_y == 0:
            velocity_x = random.randrange(-1, 1)
            velocity_y = random.randrange(-1, 1)
        self.position_x = 10
        self.position_y = 10
        self.screen = screen
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.dimensions_x = dimensions_x
        self.dimensions_y = dimensions_y

    def draw(self):
        pygame.draw.circle(self.screen.window, WHITE, self.position_x, self.position_y ,BALL_RADIUS)

    def update(self):
        self.position_x = int(self.velocity_x)
        self.position_y = int(self.velocity_y)

        if self.position_x - self.dimensions_x < -10:
            self.velocity_x *= -1
        if self.position_x + self.dimensions_x > WIDTH_GAME + 10:
            self.velocity_x *= -1
            # maybe reset and register points in collision
        # if self.position_y - self.dimensions_y < -10:
        # self.reset()
        # adaugare punctaj jucator jos
        # if self.position.y + self.dimensions_y > HEIGHT + 10:
        # self.reset()
        # adaugare punctaj bot sus

    def onCollision(self, other):
        self.velocity_x *= -1.4
