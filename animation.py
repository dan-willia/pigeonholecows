import sys
import pygame
import random
import cows

# Constants
RADIUS = 15
WIDTH = 600
HEIGHT = 600
MAX_DISTANCE = WIDTH/(2**(1/2))

SPEED = 30      #fps

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    clock = pygame.time.Clock()
    pygame.display.set_caption("Pigeonholes Cow Example")
    font = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None,18)
    text_color = (255, 255, 255) 
    
    max_min=0
    i=0
    Cows=cows.create_cows()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        i = (i + 1) % 100
        cows.change_direction(i, Cows)

        for cow in Cows:
            cow.update_pos()

        screen.fill((0,0,0)) # Background color

        # Find distance between cows and set nearest neighbor
        cows.find_nearest_neighbor(Cows)

        # Draw cows
        for cow in Cows:
            pygame.draw.circle(screen, cow.color, cow.pos, RADIUS)

        # Draw WHITE line to nearest neighbor
        for cw in Cows:
            neighbor = cw.nearest_neighbor
            # ther_cow = cows.get_cow_from_name(neighbor_name, Cows)
            pygame.draw.line(screen, (254,254,254), cw.pos, neighbor.pos, width=1)
            text_surface = font2.render(f"{cows.distance(cw,neighbor):.2f}", True, text_color)
            screen.blit(text_surface, ((cw.pos[0]+neighbor.pos[0])/2, (cw.pos[1]+neighbor.pos[1])/2))

        # Find cow with nearest nearest neighbor, draw RED line
        nn_cow = cows.find_min_distance(Cows)
        neighbor = nn_cow.nearest_neighbor
        pygame.draw.line(screen, (231,76,60), nn_cow.pos, neighbor.pos, width=1)

        cur_min = cows.distance(nn_cow, neighbor)
        if cur_min>max_min:
            max_min=cur_min

        # Display text
        text_surface = font.render(f"max min = {max_min:.2f}, max possible min = {MAX_DISTANCE:.2f}", True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH/2,25)

        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(SPEED)

if __name__ == "__main__":
    main()