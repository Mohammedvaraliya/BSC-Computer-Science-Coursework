import pygame  
pygame.init()  
screen = pygame.display.set_mode((900, 550))  
done = False  
  
#load the fonts  
font = pygame.font.SysFont("Times new Roman", 72)  
# Render the text in new surface  
text = font.render("Hello, Game Programmers", True, (200, 16, 16))  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
            done = True  
    screen.fill((255, 255, 255))  
    #We will discuss blit() in the next topic  
    screen.blit(text,(450 - text.get_width() // 2, 240 - text.get_height() // 2))  
  
    pygame.display.flip()