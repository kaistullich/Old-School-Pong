import pygame

pygame.init()
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TESTING WINDOW")
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("LEFT ARROW")
            elif event.key == pygame.K_RIGHT:
                print("RIGHT ARROW")
                x_speed = 3
            elif event.key == pygame.K_UP:
                print("UP ARROW")
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                print("DOWN ARROW")
                y_speed = 3

    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)
