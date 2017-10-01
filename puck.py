import pygame


class Puck:
    def __init__(self, w, h, screen):
        self.width = w
        self.height = h
        self.x = w / 2
        self.y = h / 2
        self.xspeed = 5
        self.yspeed = 2.5
        self.r = 12
        self.screen = screen
        self.reset()

    def show(self):
        WHITE = (255, 255, 255)
        ball_rect = pygame.Rect(self.x, self.y, self.r * 2, self.r * 2)
        pygame.draw.ellipse(self.screen, WHITE, ball_rect)

        return ball_rect

    def collide(self, p):
        # FIXME: this method only works for the right paddle
        puck = self.show()
        paddle = p.show()
        if puck.colliderect(paddle):
            if puck.centerx <= paddle.x or puck.centerx >= paddle.x + 100:
                self.xspeed *= -1
            if puck.centery <= paddle.y or puck.centery >= paddle.y + 100:
                self.yspeed *= -1

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
