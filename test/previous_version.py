import pygame


class Rectangle:

    def __init__(self, screen, coords=None, width=0):
        self.screen = screen
        self.color = (255, 255, 255)
        self.coords = coords
        self.width = width


class Circle:

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.size = 8
        self.color = (255, 255, 255)


pygame.init()

# Constants
WIDTH = 800
HEIGHT = 850
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NUMBER_OF_DIVIDERS = 30
RIGHT_X_START = 30
LEFT_X_START = 757

# window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Old School Pong")
clock = pygame.time.Clock()

info = pygame.display.Info()
swidth = info.current_w
sheight = info.current_h


def draw_environment(dividers, left_y, right_y):
    # black background
    screen.fill(BLACK)

    # create and draw the 2 paddles
    left_paddle = Rectangle(screen, coords=[RIGHT_X_START, left_y, 13, 70])
    right_paddle = Rectangle(screen, coords=[LEFT_X_START, right_y, 13, 70])
    pygame.draw.rect(screen, left_paddle.color, left_paddle.coords)
    pygame.draw.rect(screen, right_paddle.color, right_paddle.coords)

    # starting y-coord for dividers
    div_y_cord = 0
    # loop through each new Rectangle object
    for rectangle in dividers:
        rectangle.coordinates = [400, div_y_cord, 6, 20]
        # add spacing to the next y-coordinate
        div_y_cord += 30
        pygame.draw.rect(screen, rectangle.color, rectangle.coordinates)

    # create and draw the ball obj
    ball = Circle(200, 200)
    pygame.draw.circle(screen, WHITE, [ball.x, ball.y], ball.size)

    # display
    pygame.display.update()


def main():
    # create 30 rectangles for the dividers
    dividers = [Rectangle(screen) for i in range(NUMBER_OF_DIVIDERS)]

    # vertical speed
    left_paddle_y_speed = 0
    right_paddle_y_speed = 0

    # Current position
    left_paddle_y_coord = 10
    right_paddle_y_coord = 10

    while True:
        for event in pygame.event.get():
            # all keys
            keys = pygame.key.get_pressed()
            # quit game
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit()

            # check key down presses
            elif event.type == pygame.KEYDOWN:
                if keys[pygame.K_q]:
                    left_paddle_y_speed = -30
                if keys[pygame.K_a]:
                    left_paddle_y_speed = 30
                if keys[pygame.K_p]:
                    right_paddle_y_speed = -30
                if keys[pygame.K_l]:
                    right_paddle_y_speed = 30

            # user let up on a key
            elif event.type == pygame.KEYUP:
                # If it is either [Q, A, P, L] reset speed vector back to zero
                if event.key == pygame.K_q or event.key == pygame.K_a:
                    left_paddle_y_speed = 0
                elif event.key == pygame.K_p or event.key == pygame.K_l:
                    right_paddle_y_speed = 0

        # move the paddles according to the speed vector.
        left_paddle_y_coord += left_paddle_y_speed
        right_paddle_y_coord += right_paddle_y_speed

        # call the drawing environment
        draw_environment(dividers, left_paddle_y_coord, right_paddle_y_coord)

        # if left_paddle.coords[1] == HEIGHT:
        #     left_paddle_y_coord = HEIGHT
        # if left_paddle.coords[1] == 10:
        #     left_paddle_y_coord = 0
        # if right_paddle.coords[1] == HEIGHT:
        #     right_paddle_y_coord = HEIGHT
        # if right_paddle.coords[1] == 10:
        #     right_paddle_y_coord = 0

        clock.tick(120)


if __name__ == '__main__':
    main()