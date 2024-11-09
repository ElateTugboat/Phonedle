import pygame

def BoaayFunc(screen):
    
    numpad = pygame.image.load("art/numpad.png").convert()

    numpad = pygame.transform.scale(numpad, (250, 250))

    screen.blit(numpad, ((550,400)))

    
    blank_box = pygame.image.load("art/blank.png").convert()

    blank_box = pygame.transform.scale(blank_box, (250, 250))

    screen.blit(blank_box, ((0,0)))

