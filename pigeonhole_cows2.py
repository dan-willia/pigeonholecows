import sys
import pygame
import random
import cows

# Constants
RADIUS = 15
WIDTH = 600
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()
pygame.display.set_caption("Pigeonholes Cow Example")
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None,18)
text_color = (255, 255, 255) 

# Cow 1
cow_1 = cows.Cow("cow_1", (255,0,0), (20,20), 
                 (random.choice(range(-5,6)), 
                 random.choice(range(-5,6))))
# Cow 2
cow_2 = cows.Cow("cow_2", (130, 224, 170), (WIDTH-20,20),
                 (random.choice(range(-5,6)), 
                 random.choice(range(-5,6))))
# Cow 3
cow_3 = cows.Cow("cow_3", (133, 193, 233), (WIDTH-20,HEIGHT-20),
                 (random.choice(range(-5,6)), 
                 random.choice(range(-5,6))))
# Cow 4
cow_4 = cows.Cow("cow_4", (237, 187, 153), (20,HEIGHT-20),
                 (random.choice(range(-5,6)), 
                 random.choice(range(-5,6))))
# Cow 5
cow_5 = cows.Cow("cow_5", (165, 105, 189), (WIDTH/2,HEIGHT/2),
                 (random.choice(range(-5,6)), 
                 random.choice(range(-5,6))))

Cows = [cow_1,cow_2,cow_3,cow_4,cow_5]

i = 1
max_min=0
max_distance = WIDTH/(2**(1/2))

# Main loop
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

    # Draw line to nearest neighbor
    for cw in Cows:
        neighbor_name = cw.nearest_neighbor[0]
        other_cow = cows.get_cow_from_name(neighbor_name, Cows)
        pygame.draw.line(screen, (254,254,254), cw.pos, other_cow.pos, width=1)
        text_surface = font2.render(f"{cw.nearest_neighbor[1]:.2f}", True, text_color)
        screen.blit(text_surface, ((cw.pos[0]+other_cow.pos[0])/2, (cw.pos[1]+other_cow.pos[1])/2))

    # Find cow with min distance, draw line
    nn_cow = cows.find_min_distance(Cows)
    other_cow_name = nn_cow.nearest_neighbor[0]
    other_cow = cows.get_cow_from_name(other_cow_name, Cows)
    pygame.draw.line(screen, (231,76,60), nn_cow.pos, other_cow.pos, width=1)

    cur_min = nn_cow.nearest_neighbor[1]
    if cur_min>max_min:
        max_min=cur_min

    # Display text
    text_surface = font.render(f"max min = {max_min:.2f}, max possible min = {max_distance:.2f}", True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (300,25)

    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(20)