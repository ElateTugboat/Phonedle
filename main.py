import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

tangerine_font = pygame.font.Font("Fonts/Tangerine-Bold.ttf", 50)
pb_font = pygame.font.Font("Fonts/Peanut Butter.ttf", 40)
title_font_color = (255, 255, 255)
name = "Bill Johnson"

title_surface = tangerine_font.render("Phonedle", True, title_font_color)
objective_text_surface = pb_font.render(f"Guess the number of:", True, title_font_color)
name_surface = pb_font.render(f"{name}", True, title_font_color)

screen_width, screen_height = screen.get_size()
title_width, title_height = title_surface.get_size()
objective_text_width, objective_text_height = objective_text_surface.get_size()
name_width, name_height = name_surface.get_size()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg_color = (18, 18, 76)
    screen.fill(bg_color)

    
    image = pygame.image.load("boaay/Kream.png").convert()
    
    screen.blit(image,(10,10))
    
    screen.blit(title_surface, ((screen_width - title_width) / 2, (screen_height - title_height) / 2 - 250))
    screen.blit(objective_text_surface, ((screen_width - objective_text_width) / 2, (screen_height - objective_text_height) / 2 - 105))
    screen.blit(name_surface, ((screen_width - name_width) / 2, (screen_height - name_height) / 2 - 65))
    
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
