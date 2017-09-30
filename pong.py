import pygame

from paddle import Paddle
from puck import Puck

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 480
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption("Old School Pong")
clock = pygame.time.Clock()

# create a puck
puck = Puck(WIDTH, HEIGHT, screen)

# create 2 paddles
left = Paddle(screen, HEIGHT, WIDTH, RED, True)
right = Paddle(screen, HEIGHT, WIDTH, GREEN, False)


def draw():
    # black background
    screen.fill(BLACK)

    # puck.checkPaddle(left)
    puck.checkPaddleLeft(right)

    # show the 2 paddles on window
    left.show()
    right.show()

    # move the puck around the window
    puck.update()

    # show and restrict edges for puck
    puck.edges()
    puck.show()

    # display
    pygame.display.update()


def main():
    # flags for key press events
    q_down = False
    a_down = False
    p_down = False
    l_down = False

    yspeed = 18

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
                # left paddle
                if event.key == pygame.K_q:
                    q_down = True
                elif event.key == pygame.K_a:
                    a_down = True

                # right paddle
                elif event.key == pygame.K_p:
                    p_down = True
                elif event.key == pygame.K_l:
                    l_down = True

            # user let up on a key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q or event.key == pygame.K_a:
                    q_down = False
                    a_down = False
                elif event.key == pygame.K_p or event.key == pygame.K_l:
                    p_down = False
                    l_down = False

        # check if paddles should be moving up/down (key held down)
        # FIXME: maybe there is a more OOP approach to this?
        # left paddle
        if q_down:
            left.move(-yspeed)
        if a_down:
            left.move(yspeed)
        # right paddle
        if p_down:
            right.move(-yspeed)
        if l_down:
            right.move(yspeed)

        # check to stop paddles from moving (key NOT held down)
        # FIXME: maybe there is a more OOP approach to this?
        # left paddle
        if not q_down or not a_down:
            left.move(0)
        # right paddle
        if not p_down or not l_down:
            right.move(0)

        # call animation function
        draw()

        # FPS
        clock.tick(50)


if __name__ == '__main__':
    main()
