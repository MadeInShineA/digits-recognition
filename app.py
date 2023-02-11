import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 500))

drawing_area = pygame.Rect(500, 0, 500, 500)
pygame.draw.rect(screen, "white", (500,0,500,500), 0)



pygame.display.set_caption("Image recognition")

game_running = True

my_font = pygame.font.Font(None, 30)

text = []

basic_text_surface = my_font.render('Ai predictions : ', True, "white")
basic_text_rect = basic_text_surface.get_rect(center=(500 / 2, 20))

text.append((basic_text_surface,basic_text_rect))

zero_text_surface = my_font.render('0 : ', True, "white")
zero_text_rect = basic_text_surface.get_rect(center=(100, 40))

text.append((zero_text_surface,zero_text_rect))

one_text_surface = my_font.render('1 : ', True, "white")
one_text_rect = basic_text_surface.get_rect(center=(100, 70))

text.append((one_text_surface,one_text_rect))

two_text_surface = my_font.render('2 : ', True, "white")
two_text_rect = basic_text_surface.get_rect(center=(100, 100))

text.append((two_text_surface,two_text_rect))

tree_text_surface = my_font.render('3 : ', True, "white")
tree_text_rect = basic_text_surface.get_rect(center=(100, 130))

text.append((tree_text_surface,tree_text_rect))

four_text_surface = my_font.render('4 : ', True, "white")
four_text_rect = basic_text_surface.get_rect(center=(100, 160))

text.append((four_text_surface,four_text_rect))


five_text_surface = my_font.render('5 : ', True, "white")
five_text_rect = basic_text_surface.get_rect(center=(100, 190))

text.append((five_text_surface,five_text_rect))

six_text_surface = my_font.render('6 : ', True, "white")
six_text_rect = basic_text_surface.get_rect(center=(100, 220))

text.append((six_text_surface,six_text_rect))

seven_text_surface = my_font.render('7 : ', True, "white")
seven_text_rect = basic_text_surface.get_rect(center=(100, 250))

text.append((seven_text_surface,seven_text_rect))

eight_text_surface = my_font.render('8 : ', True, "white")
eight_text_rect = basic_text_surface.get_rect(center=(100, 280))

text.append((eight_text_surface,eight_text_rect))

nine_text_surface = my_font.render('9 : ', True, "white")
nine_text_rect = basic_text_surface.get_rect(center=(100, 310))
def display_text ():
    for surface, rect in text:
        screen.blit(surface, rect)







while game_running:
    pygame.draw.rect(screen, "black", (0, 0, 500, 500), 0)
    display_text()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    if pygame.mouse.get_pressed() == (1, 0, 0):
        mouse_position = pygame.mouse.get_pos()
        if drawing_area.collidepoint(mouse_position):
            pygame.draw.circle(surface=screen, center=mouse_position, color="black", radius=7)
    if pygame.mouse.get_pressed() == (0, 0, 1):
        mouse_position = pygame.mouse.get_pos()
        if drawing_area.collidepoint(mouse_position):
            pygame.draw.circle(surface=screen, center=mouse_position, color="white", radius=10)
    if pygame.mouse.get_pressed() == (0, 1, 0):
        mouse_position = pygame.mouse.get_pos()
        if drawing_area.collidepoint(mouse_position):
            pygame.draw.rect(screen, "white", (500,0,500,500), 0)

    pygame.display.flip()