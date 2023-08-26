import pygame  
pygame.init()  
# sets the window title  
pygame.display.set_caption(u'Keyboard events')  
# sets the window size  
pygame.display.set_mode((900, 550))  
  
while True:  
    # gets a single event from the event queue  
    event = pygame.event.wait()  
    # if the 'close' button of the window is pressed  
    if event.type == pygame.QUIT:  
        # stops the application  
        break  
    # Detects the 'KEYDOWN' and 'KEYUP' events  
    if event.type in (pygame.KEYDOWN, pygame.KEYUP):  
        # gets the key name  
        key_name = pygame.key.name(event.key)  
        # converts to uppercase the key name  
        key_name = key_name.upper()  
        # if any key is pressed  
        if event.type == pygame.KEYDOWN:  
            # prints on the console the key pressed  
            print(u'"{}" key pressed'.format(key_name))  
        # if any key is released  
        elif event.type == pygame.KEYUP:  
            # prints on the console the released key  
            print(u'"{}" key released'.format(key_name))