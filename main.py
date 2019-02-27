import pygame
import math
import random

from fish import *
from vector import Vector2D

def main():

    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))

    fishes = list()

    """
    fishes.append(Fish())
    fishes.append(Fish())
    fishes[0].pos.y = 50
    fishes[0].vel.y = 50
    fishes[-1].vel.x = 50

    """
    for x in range(0,50):
        fishes.append(Fish())
        fishes[-1].pos.x = random.randint(-200,200)
        fishes[-1].pos.y = random.randint(-200,200)
        angle = random.random() * 2 * math.pi
        fishes[-1].vel.x = fishes[-1].swim_speed * math.cos(angle)
        fishes[-1].vel.y = fishes[-1].swim_speed * math.sin(angle)


    window_size = Vector2D(1000, 1000)
    origin = Vector2D(0, 0)

    fps = 60
    time_per_frame = 1 / fps
    
    clock = pygame.time.Clock()
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        # clear screen
        screen.fill((0,0,0))

        # draw fish
        for fish in fishes:
            pygame.draw.circle(screen, (255, 255, 255),
                    (int((fish.pos.x + window_size.x) // 2), int((fish.pos.y + window_size.y) // 2)), fish.size)
            fish.findNearbyFish(fishes)
        for fish in fishes:
            fish.updateVel(fish.getNewAngle(fish.findAngle_COM(), time_per_frame))
        for fish in fishes:
            fish.swim(time_per_frame)
        
        pygame.display.flip()
        clock.tick(fps)
        


if __name__ == "__main__":
    main()