import pygame
from Pong import *

pygame.init()

WIDTH = 800
HEIGHT = 850
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NUMBER_OF_DIVIDERS = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Old School Pong")
clock = pygame.time.Clock()


def draw_environment(dividers):
    # black background
    screen.fill(BLACK)

    # create and draw the 2 paddles
    # TODO: figure out how to make the paddles move with up arrows
    paddle1 = Rectangle(screen, coords=[30, 350, 13, 70])
    paddle2 = Rectangle(screen, coords=[757, 350, 13, 70])
    pygame.draw.rect(screen, paddle1.color, paddle1.coords)
    pygame.draw.rect(screen, paddle2.color, paddle2.coords)

    # starting y-coordinate for dividers
    y_cord = 0
    # loop through each new Rectangle object
    for rectangle in dividers:
        # create coordinates for each rectangle
        rectangle.coordinates = [400, y_cord, 6, 20]
        # add spacing to the next y-coordinate
        y_cord += 30
        # draw divider rectangles
        pygame.draw.rect(screen, rectangle.color, rectangle.coordinates)

    # create and draw the ball obj
    # TODO: figure out how to make the ball move, and make ball bounce off walls
    ball = Circle(200, 200)
    pygame.draw.circle(screen, WHITE, [ball.x, ball.y], ball.size)

    # display
    pygame.display.update()


def main():
    """ Main function for starting the pygame surface """

    # create 30 rectangles for the dividers
    dividers = [Rectangle(screen) for i in range(NUMBER_OF_DIVIDERS)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment(dividers)
        clock.tick(60)


if __name__ == '__main__':
    main()
