import pygame


class Paddle:

    def __init__(self, screen, window_h, window_w, left_paddle):
        self.screen = screen
        self.width = window_w
        self.y = window_h / 2
        self.pad_width = 10
        self.pad_height = 70
        self.window_h = window_h

        if left_paddle:
            self.x = self.pad_width / 2
        else:
            self.x = self.width - self.pad_width * 1.5

    def show(self):
        WHITE = (255, 255, 255)
        rect = pygame.Rect(self.x, self.y, self.pad_width, self.pad_height)
        pygame.draw.rect(self.screen, WHITE, rect)

    def move(self, speed):
        self.y += speed
        # check if the paddle is off screen
        if self.y < 0:
            self.y = 0
        if self.y > self.window_h - self.pad_height:
            self.y = self.window_h - self.pad_height
