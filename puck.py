import pygame
import math


class Puck:
    def __init__(self, w, h, screen):
        self.width = w
        self.height = h
        self.x = w / 2
        self.y = h / 2
        self.xspeed = 5
        self.yspeed = 1
        self.r = 12
        self.screen = screen
        self.reset()

    def checkPaddleLeft(self, p):
        if self.y - self.r < p.y + p.pad_height / 2 and self.y + self.r > p.y - p.pad_height / 2 and self.x - self.r < p.x + p.pad_width / 2:
            if self.x > p.x:
                diff = self.y - (p.y - p.pad_height / 2)
                rad = math.radians(45)
                # TODO: Continue here
                angle = map()

    def show(self):
        WHITE = (255, 255, 255)
        pygame.draw.ellipse(self.screen, WHITE, (self.x, self.y, self.r * 2, self.r * 2))

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed

    def reset(self):
        self.x = self.width / 2
        self.y = self.height / 2

    def edges(self):
        if self.y < 0 or self.y > self.height - 24:
            self.yspeed *= -1
        if self.x > self.width - 24:
            self.reset()
        if self.x < 0:
            self.reset()
