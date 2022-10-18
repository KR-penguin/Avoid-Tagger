# Made by KOPENG

import pygame
import random

def Setup_Screen(a, b):
    global screen_width
    global screen_height
    global screen

    screen_width = a
    screen_height = b
    screen = pygame.display.set_mode((screen_width, screen_height))

def Setup_variable():
    global level
    global clock

    level = 0
    clock = pygame.time.Clock()

def Setup_Background():
    global background
    global background_X_pos
    global background_Y_pos

    background = pygame.image.load("./image/Background.png")
    background_X_pos = 0
    background_Y_pos = 0

def Setup_Character():
    global character
    global character_size
    global character_width
    global character_height
    global character_X_pos
    global character_Y_pos

    
    character = pygame.image.load("./image/character.png")
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_X_pos = screen_width / 2
    character_Y_pos = screen_height / 2

def Draw_object():
    global background
    global background_X_pos
    global background_Y_pos
    global character
    global character_X_pos
    global character_Y_pos

    screen.blit(background, (background_X_pos, background_Y_pos))
    screen.blit(character, (character_X_pos, character_Y_pos))

def Setup_Character_KeyboardEvent():
    global character_to_X
    global character_to_Y

    character_to_X = 0
    character_to_Y = 0

def Perceive_KeyboardEvent():
    global character_to_X
    global character_to_Y

    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_a: 
            character_to_X -= 1
        elif event.key == pygame.K_d: 
            character_to_X += 1
        elif event.key == pygame.K_w: 
            character_to_Y -= 1
        elif event.key == pygame.K_s: 
            character_to_Y += 1

    if event.type == pygame.KEYUP: 
        if event.key == pygame.K_a or event.key == pygame.K_d:
            character_to_X = 0
        elif event.key == pygame.K_w or event.key == pygame.K_s:
            character_to_Y = 0

def Move_Character():
    global character_to_X
    global character_to_Y
    global character_X_pos
    global character_Y_pos

    character_X_pos += character_to_X
    character_Y_pos += character_to_Y

pygame.init()

Setup_Screen(600, 600)
Setup_variable()
Setup_Background()
Setup_Character()
Setup_Character_KeyboardEvent()
pygame.display.set_caption("Hide & Seek")

# main loop

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        Perceive_KeyboardEvent()


    Move_Character()
    Draw_object()
    pygame.display.update()

pygame.quit()

# FPS 부분부터 구현시작하면 됨