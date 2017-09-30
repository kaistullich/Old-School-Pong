import pygame


class Paddle:

    def __init__(self, screen, window_h, window_w, color, left_paddle):
        self.screen = screen
        self.y = window_h / 2
        self.pad_width = 10
        self.pad_height = 70
        self.color = color
        self.window_w = window_w
        self.window_h = window_h

        if left_paddle:
            self.x = self.pad_width / 2
        else:
            self.x = self.window_w - (self.pad_width * 1.5)

    def show(self):
        rect = pygame.Rect(self.x, self.y, self.pad_width, self.pad_height)
        pygame.draw.rect(self.screen, self.color, rect)

    def move(self, speed):
        self.y += speed
        # check if the paddle is off screen
        if self.y < 0:
            self.y = 0
        if self.y > self.window_h - self.pad_height:
            self.y = self.window_h - self.pad_height
