import pygame
from Clockwork import *
from boaay import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

tangerine_font = pygame.font.Font("Fonts/Tangerine-Bold.ttf", 50)
pb_font = pygame.font.Font("Fonts/Peanut Butter.ttf", 40)
WHITE = (255, 255, 255)

# Text
title_surface = tangerine_font.render("Phonedle", True, WHITE)
objective_text_surface = pb_font.render(f"Guess the number of:", True, WHITE)
name_surface = pb_font.render(f"{Clockwork.contact1['name']}", True, WHITE)

# Images
blank_box = pygame.image.load("art/blank.png").convert()
kindof_box = pygame.image.load("art/kindof.png").convert()
right_box = pygame.image.load("art/right.png").convert()
wrong_box = pygame.image.load("art/wrong.png").convert()

# Shapes
input_box = pygame.Rect(100, 150, 400, 50)

screen_width, screen_height = screen.get_size()
title_width, title_height = title_surface.get_size()
objective_text_width, objective_text_height = objective_text_surface.get_size()
name_width, name_height = name_surface.get_size()

phone_number = ""
max_len = 10

def render_text(text, font, color):
    return font.render(text, True, color)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg_color = (18, 18, 76)
    screen.fill(bg_color)
    
    screen.blit(title_surface, ((screen_width - title_width) / 2, (screen_height - title_height) / 2 - 250))
    screen.blit(objective_text_surface, ((screen_width - objective_text_width) / 2, (screen_height - objective_text_height) / 2 - 105))
    screen.blit(name_surface, ((screen_width - name_width) / 2, (screen_height - name_height) / 2 - 65))
    
    BoaayFunc(screen)
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
