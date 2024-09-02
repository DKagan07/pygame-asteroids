import pygame
from constants import *
from player import Player


def main():
    """main function is our main function"""

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # This checks if the user has closed the window
        # AKA makes the X (close) button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill(color=pygame.Color(0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # sets FPS to 60
        dt = fps.tick(60) / 1000


# ensures main() is only called when this file is run directly
if __name__ == "__main__":
    main()
