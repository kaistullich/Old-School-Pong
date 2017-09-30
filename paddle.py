import pygame


class Paddle:

    def __init__(self, screen, h, w, left):
        self.screen = screen
        self.width = w
        self.y = h / 2
        self.pad_width = 10
        self.pad_height = 70

        if left:
            self.x = self.pad_width / 2
        else:
            self.x = self.width - self.pad_width * 1.5

    def show(self):
        WHITE = (255, 255, 255)
        rect = pygame.Rect(self.x, self.y, self.pad_width, self.pad_height)
        # FIXME: this clamp does not function properly
        # rect.clamp_ip(self.screen.get_rect())
        pygame.draw.rect(self.screen, WHITE, rect)

    def move(self, speed):
        self.y += speed
