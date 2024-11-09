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
ORANGE = (255, 128, 0)

# Misc
ans_check = False

# Text
title_surface = tangerine_font.render("Phonedle", True, WHITE)
objective_text_surface = pb_font.render(f"Guess the number of:", True, WHITE)
name_surface = pb_font.render(f"{Clockwork.contact1['name']}", True, WHITE)
user_text = ""

# Images
blank_box = pygame.image.load("art/blank.png").convert()
kindof_box = pygame.image.load("art/kindof.png").convert()
right_box = pygame.image.load("art/right.png").convert()
wrong_box = pygame.image.load("art/wrong.png").convert()

# Shapes
input_box = pygame.Rect(100, 150, 400, 50)
input_rect = pygame.Rect(200, 200, 140, 32) 

screen_width, screen_height = screen.get_size()
title_width, title_height = title_surface.get_size()
objective_text_width, objective_text_height = objective_text_surface.get_size()
name_width, name_height = name_surface.get_size()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN: 

            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 

                # get text input from 0 to -1 i.e. end. 
                user_text = user_text[:-1] 
            
            elif event.key == pygame.K_RETURN:
                if user_text == Clockwork.contact1["number"]:
                    user_text = ""
                    bg_color = (0, 204, 102)
                

            # Unicode standard is used for string 
            # formation 
            else: 
                user_text += event.unicode

    if ans_check == False:
        bg_color = (18, 18, 76)
    screen.fill(bg_color)
    
    screen.blit(title_surface, ((screen_width - title_width) / 2, (screen_height - title_height) / 2 - 250))
    screen.blit(objective_text_surface, ((screen_width - objective_text_width) / 2, (screen_height - objective_text_height) / 2 - 105))
    screen.blit(name_surface, ((screen_width - name_width) / 2, (screen_height - name_height) / 2 - 65))
    
    pygame.draw.rect(screen, ORANGE, input_rect) 
  
    text_surface = pb_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
    # set width of textfield so that text cannot get 
    # outside of user's text input 
    input_rect.w = max(100, text_surface.get_width()+10) 
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
