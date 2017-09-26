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

# useful information for walls later on
info = pygame.display.Info()
swidth = info.current_w
sheight = info.current_h


def draw_environment(dividers, y_loc):
    # black background
    screen.fill(BLACK)

    # create and draw the 2 paddles
    # TODO: figure out how to make the paddles move with up arrows
    paddle1 = Rectangle(screen, coords=[30, y_loc, 13, 70])
    paddle2 = Rectangle(screen, coords=[757, y_loc, 13, 70])
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

    y_move = int(HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            # all keys
            keys = pygame.key.get_pressed()

            # quit game
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit()

            # check key presses
            elif event.type == pygame.KEYDOWN:
                # TODO: adjust the paddles to go up/down with key presses
                if keys[pygame.K_a]:
                    print("Left Paddle 'A' pressed")
                if keys[pygame.K_q]:
                    print("Left Paddle 'Q' pressed")
                if keys[pygame.K_p]:
                    print("Right paddle 'P' pressed")
                if keys[pygame.K_l]:
                    print("Right paddle 'L' pressed")

        draw_environment(dividers, y_move)
        y_move += 50
        clock.tick(60)


if __name__ == '__main__':
    main()
