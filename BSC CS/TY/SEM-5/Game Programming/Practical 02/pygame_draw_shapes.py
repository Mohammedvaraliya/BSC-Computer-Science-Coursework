import pygame  
from math import pi  
pygame.init()  
# size variable is using for set screen size  
size = [900, 550]  
screen = pygame.display.set_mode(size)  
pygame.display.set_caption("Example program to draw geometry")  
# done variable is using as flag   
done = False  
clock = pygame.time.Clock()  
while not done:  
    # clock.tick() limits the while loop to a max of 10 times per second.  
    clock.tick(10)
  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True 
    screen.fill((0, 0, 0))  

    pygame.draw.line(screen, (0, 255, 0), [0, 0], [50, 30], 5)  
    pygame.draw.lines(screen, (0, 0, 0), False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5) 
    pygame.draw.rect(screen, (0, 0, 0), [75, 10, 50, 20], 2)
    pygame.draw.rect(screen, (0, 0, 0), [150, 10, 50, 20])
    pygame.draw.ellipse(screen, (255, 0, 0), [225, 10, 50, 20], 2)
    pygame.draw.ellipse(screen, (255, 0, 0), [300, 10, 50, 20])
    pygame.draw.polygon(screen, (0, 0, 0), [[100, 100], [0, 200], [200, 200]], 5)
    pygame.draw.circle(screen, (0, 0, 255), [60, 250], 40)
    pygame.draw.arc(screen, (0, 0, 0), [210, 75, 150, 125], 0, pi / 2, 2)
    pygame.display.flip()  
  
# Quite the execution when clicking on close  
pygame.quit()