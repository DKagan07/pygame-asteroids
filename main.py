import pygame
from constants import *
from player import Player


def main():
    """main function is our main function"""

    pygame.init()
    fps = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # This checks if the user has closed the window
        # AKA makes the X (close) button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=pygame.Color(0, 0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        # sets FPS to 60
        dt = fps.tick(60) / 1000


# ensures main() is only called when this file is run directly
if __name__ == "__main__":
    main()
