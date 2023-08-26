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
  
    for event in pygame.event.get():  # User did something  
        if event.type == pygame.QUIT:  # If user clicked on close symbol   
            done = True  # done variable that we are complete, so we exit this loop  

    # All drawing code occurs after the for loop and but  
    # inside the main while done==False loop.  

    # Clear the default screen background and set the white screen background  
    screen.fill((0, 0, 0))  

    # Draw on the screen a green line which is 5 pixels wide.  
    pygame.draw.line(screen, (0, 255, 0), [0, 0], [50, 30], 5)  
    # Draw on the screen a green line which is 5 pixels wide.  
    pygame.draw.lines(screen, (0, 0, 0), False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)  

    # Draw a rectangle outline  
    pygame.draw.rect(screen, (0, 0, 0), [75, 10, 50, 20], 2)  

    # Draw a solid rectangle  
    pygame.draw.rect(screen, (0, 0, 0), [150, 10, 50, 20])  

    # This draw an ellipse outline, using a rectangle as the outside boundaries  
    pygame.draw.ellipse(screen, (255, 0, 0), [225, 10, 50, 20], 2)  

    # This draw a solid ellipse, using a rectangle as the outside boundaries  
    pygame.draw.ellipse(screen, (255, 0, 0), [300, 10, 50, 20])  

    # Draw a triangle using the polygon function  
    pygame.draw.polygon(screen, (0, 0, 0), [[100, 100], [0, 200], [200, 200]], 5)  

    # This draw a circle  
    pygame.draw.circle(screen, (0, 0, 255), [60, 250], 40)  

    # This draw an arc  
    pygame.draw.arc(screen, (0, 0, 0), [210, 75, 150, 125], 0, pi / 2, 2)  

    # This function must write after all the other drawing commands.  
    pygame.display.flip()  
  
# Quite the execution when clicking on close  
pygame.quit()