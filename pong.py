import pygame
from puck import Puck
from paddle import Paddle

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption("Old School Pong")
clock = pygame.time.Clock()

# create a puck
puck = Puck(WIDTH, HEIGHT, screen)

# create 2 paddles
left = Paddle(screen, HEIGHT, WIDTH, True)
right = Paddle(screen, HEIGHT, WIDTH, False)


def draw():
    # black background
    screen.fill(BLACK)

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
    while True:
        # all keys
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit()

            # check key down presses
            elif event.type == pygame.KEYDOWN:
                # left paddle
                if keys[pygame.K_a]:
                    left.move(-50)
                if keys[pygame.K_z]:
                    left.move(50)

                # right paddle
                if keys[pygame.K_j]:
                    right.move(-50)
                if keys[pygame.K_m]:
                    right.move(50)

            # user let up on a key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z or event.key == pygame.K_a:
                    left.move(0)
                elif event.key == pygame.K_j or event.key == pygame.K_m:
                    right.move(0)

        # call animation function
        draw()

        # FPS
        clock.tick(120)


if __name__ == '__main__':
    main()
