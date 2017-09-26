import pygame
from Pong import *

pygame.init()

WIDTH = 800
HEIGHT = 850
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Old School Pong")
clock = pygame.time.Clock()


def draw_environment():
    # black background
    screen.fill(BLACK)

    # create the 2 paddles
    paddle1 = Rectangles(screen, WHITE, [15, 350, 6, 80])
    paddle2 = Rectangles(screen, WHITE, [760, 350, 6, 80])

    # draw the paddles
    paddle1.draw_rect(pygame)
    paddle2.draw_rect(pygame)

    # display
    pygame.display.update()


def main():
    """ Main function for starting the pygame surface """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment()
        clock.tick(60)


if __name__ == '__main__':
    main()
