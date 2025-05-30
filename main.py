import pygame
from constants import *


def main():
    # make a while loop
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Infinite game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Fill screen with black
        screen.fill('black') 

        # Update display
        pygame.display.flip()


if __name__ == "__main__":
    main()
