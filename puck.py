import pygame


class Puck:
    def __init__(self, w, h, screen):
        self.width = w
        self.height = h
        self.x = w / 2
        self.y = h / 2
        self.xspeed = 1
        self.yspeed = 3
        self.screen = screen

    def show(self):
        WHITE = (255, 255, 255)
        pygame.draw.ellipse(self.screen, WHITE, (self.x, self.y, 24, 24))

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
