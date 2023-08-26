import pygame  
pygame.init()  
white = (255, 255, 255)  
# assigning values to height and width variable   
height = 550 
width = 900
# creating the display surface object   
# of specific dimension..e(X, Y).   
display_surface = pygame.display.set_mode((width, height))  
  
# set the pygame window name   
pygame.display.set_caption('Image')  
  
# creating a surface object, image is drawn on it.   
image = pygame.image.load(r'Practical 02\assets\gaming-virtual-blue-adobestock.webp')  
  
# infinite loop   
while True:  
    display_surface.fill(white)  
    display_surface.blit(image, (0, 0))  
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()  
        # Draws the surface object to the screen.   
        pygame.display.update()