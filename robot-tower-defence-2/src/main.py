import pygame


DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 576


def main():
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Robot Invasion Defence II")

    pygame.init()

    running = True
    while running:
        pygame.display().update()

    pygame.quit()


if __name__ == "__main__":
    main()
