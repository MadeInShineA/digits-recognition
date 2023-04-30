import pygame
import tensorflow as tf
from PIL import Image
import numpy as np
import os
from tensorflow.python.ops.numpy_ops import np_config

np_config.enable_numpy_behavior()

model = tf.keras.models.load_model('final-cnn-digits-model')

pygame.init()
screen = pygame.display.set_mode((1000, 500))

drawing_area = pygame.Rect(500, 0, 500, 500)
pygame.draw.rect(screen, "black", (500,0,500,500), 0)

pygame.display.set_caption("Digits recognition")

game_running = True

my_font = pygame.font.Font(None, 30)

text = []

basic_text_surface = my_font.render('Ai predictions : ', True, "white")
basic_text_rect = basic_text_surface.get_rect(center=(500 / 2, 20))

text.append((basic_text_surface,basic_text_rect))

for i in range(10):
    surface = my_font.render(str(i)+" : ", True, "white")
    rect = basic_text_surface.get_rect(center=(100, ((i+1)*30)+10))
    text.append((surface, rect))

def display_text ():
    for surface, rect in text:
        screen.blit(surface, rect)

def save_image():
    sub = screen.subsurface(drawing_area)
    pygame.image.save(sub, "image.jpg")
def predict():
    img = Image.open("image.jpg").convert('L').resize((28, 28))
    img = np.array(img)
    img = img/255
    predictions = model(img[None, :, :]).tolist()
    return predictions
def update_predictions(predictions):
    index = 0
    max_index = np.where(predictions[0] == np.amax(predictions[0]))
    for surface, rect in text[1:]:
        text.remove((surface, rect))
        if index == max_index[0]:
            text_color = "green"
        else:
            text_color = "white"
        surface = my_font.render(str(index) +" : "+ str(round(predictions[0][index] *100, 2))+" %", True, text_color)
        text.append((surface, rect))
        index +=1

while game_running:
    pygame.draw.rect(screen, "black", (0, 0, 480, 500), 0)
    pygame.draw.rect(screen, "white", (480, 0, 20, 500), 0)
    display_text()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if os.path.exists("image.jpg"):
                os.remove("image.jpg")
            game_running = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            if drawing_area.collidepoint(mouse_position):
                save_image()
                predictions = predict()
                update_predictions(predictions)

    if pygame.mouse.get_pressed() == (1, 0, 0):
        mouse_position = pygame.mouse.get_pos()
        if drawing_area.collidepoint(mouse_position):
            pygame.draw.circle(surface=screen, center=mouse_position, color="white", radius=12)

    if pygame.mouse.get_pressed() == (0, 0, 1):
        mouse_position = pygame.mouse.get_pos()
        if drawing_area.collidepoint(mouse_position):
            pygame.draw.circle(surface=screen, center=mouse_position, color="black", radius=12)

    if pygame.mouse.get_pressed() == (0, 1, 0):
        mouse_position = pygame.mouse.get_pos()
        if drawing_area.collidepoint(mouse_position):
            pygame.draw.rect(screen, "black", (500,0,500,500), 0)

    pygame.display.flip()