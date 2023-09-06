import pygame
from particle import Particle

FPS = 60
SCREEN_SIZE = 800
BACKGROUND = (0, 0, 0)
QUANTITY = 50
RADIUS = 5


def main():
    particles = [
        Particle(particle_id, RADIUS, SCREEN_SIZE)
        for particle_id in range(QUANTITY)
    ]

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Collisions")
    clock = pygame.time.Clock()

    running = True
    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(BACKGROUND)

        # RENDER YOUR GAME HERE
        for particle in particles:
            particle.update(clock.get_time() / 100, particles)
            pygame.draw.circle(screen, particle.color, particle.position, particle.radius)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS

    pygame.quit()


if __name__ == "__main__":
    main()
