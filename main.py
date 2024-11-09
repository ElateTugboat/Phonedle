import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

arial_font = pygame.font.Font("Fonts/Tangerine-Bold.ttf", 50)
title_font_color = (255, 255, 255)

title_surface = arial_font.render("Phonedle", True, title_font_color)

screen_width, screen_height = screen.get_size()
text_width, text_height = title_surface.get_size()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg_color = (18, 18, 76)
    screen.fill(bg_color)

    
    image = pygame.image.load("boaay/Kream.png").convert()
    
    screen.blit(image,(10,10))
    
    screen.blit(title_surface, ((screen_width - text_width) / 2, (screen_height - text_height) / 2 - 250))
    
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

