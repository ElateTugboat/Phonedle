import pygame
from Clockwork import *
from boaay import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

tangerine_font = pygame.font.Font("Fonts/Tangerine-Bold.ttf", 50)
pb_font = pygame.font.Font("Fonts/Peanut Butter.ttf", 40)

colors = {
    "WHITE": (255, 255, 255),
    "ORANGE": (255, 128, 0)
}

# Misc
ans_check = False

# Text


def render_text(font, text, color):
    return font.render(text, True, color)


title_surface = render_text(tangerine_font, "Phonedle", "WHITE")
objective_text_surface = render_text(pb_font, "Guess the number of:", "WHITE")
name_surface = pb_font.render(f"{Clockwork.contact1['name']}", True, "WHITE")
user_text = ""

# Images
image_paths = {
    "blank": "art/blank.png",
    "kindof": "art/kindof.png",
    "right": "art/right.png",
    "wrong": "art/wrong.png"
}

images = {key: pygame.image.load(path).convert()
          for key, path in image_paths.items()}

# Shapes
input_box = pygame.Rect(100, 150, 400, 50)


screen_width, screen_height = screen.get_size()
title_width, title_height = title_surface.get_size()
objective_text_width, objective_text_height = objective_text_surface.get_size()
name_width, name_height = name_surface.get_size()
input_rect = pygame.Rect((screen_width - objective_text_width) / 2,
                         (screen_height - objective_text_height) / 2 + 30, 140, 32)

numkey = pygame.image.load("art/kindof.png").convert()
numkey_rect = numkey.get_rect()

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
                if user_text == Clockwork.contact1['number']:
                    ans_check = True
                    bg_color = (0, 204, 102)
                else:
                    user_text = ""

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
    
    def numkey_click(num_pressed):
        global user_text
        user_text += str(num_pressed)
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            mouse_pos = event.pos
            if numkey_rect.collidepoint(mouse_pos):
                numkey_click(1)

    if ans_check == False:
        bg_color = (18, 18, 76)
    screen.fill(bg_color)

    screen.blit(title_surface, ((screen_width - title_width) /
                2, (screen_height - title_height) / 2 - 250))
    screen.blit(objective_text_surface, ((screen_width - objective_text_width) /
                2, (screen_height - objective_text_height) / 2 - 105))
    screen.blit(name_surface, ((screen_width - name_width) /
                2, (screen_height - name_height) / 2 - 65))
    screen.blit(numkey, (450, 500))
    numkey_rect.topleft = 450, 500

    BoaayFunc(screen)
    pygame.draw.rect(screen, "ORANGE", input_rect)

    text_surface = pb_font.render(user_text, True, (61, 63, 120))

    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
