import pygame

def BoaayFunc(screen):
    
    numpad = pygame.image.load("art/numpad.png").convert()
    

    numpad = pygame.transform.scale(numpad, (200, 200))

    screen.blit(numpad, ((550,450)))

    DrawBoxLine([100,350], 10, 100, screen)


def DrawBoxLine(pos, lenth, step, screen):

    i = 0
    
    scale_both = 80

    scale = (scale_both, scale_both)

    while i < lenth:
        pos[0] = pos[0] + step
        
        blank_box = pygame.image.load("art/blank.png").convert()

    


        blank_box = pygame.transform.scale(blank_box, scale)

        screen.blit(blank_box, ((pos[0] , pos[1] )))
        i += 1

