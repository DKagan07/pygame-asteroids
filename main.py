import pygame
from constants import *


def main():
    """main function is our main function"""

    pygame.init()
    fps = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # This checks if the user has closed the window
        # AKA makes the X (close) button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=pygame.Color(0, 0, 0))
        pygame.display.flip()

        # sets framerate
        t = fps.tick(60)
        dt = t / 1000


# ensures main() is only called when this file is run directly
if __name__ == "__main__":
    main()
