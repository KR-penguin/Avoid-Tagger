# Made by KOPENG

import pygame
import random
import time

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
    global enemy_direction_decision
    global playtime
    global score

    level = 0
    clock = pygame.time.Clock()
    enemy_direction_decision = 0
    playtime = 0
    score = 0

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
    character_X_pos = screen_width / 2 - character_width / 2
    character_Y_pos = screen_height - character_height - 100

def Setup_Enemy():
    global enemy
    global enemy_size
    global enemy_width
    global enemy_height
    global enemy_X_pos
    global enemy_Y_pos
    global enemy_to_X
    global enemy_to_Y
    global level
    global enemy_speed

    if level == 1:
        enemy = pygame.image.load("./image/enemy_easy.png")
    elif level == 2:
        enemy = pygame.image.load("./image/enemy_normal.png")
    elif level == 3:
        enemy = pygame.image.load("./image/enemy_hard.png")
    elif level == 4:
        enemy = pygame.image.load("./image/enemy_hardcore.png")
    else:
        print("오류 발생 (error code : 002)")
        print("프로그램을 종료합니다...")
        exit()

    enemy_size = enemy.get_rect().size 
    enemy_width = enemy_size[0] 
    enemy_height = enemy_size[1] 
    enemy_X_pos = screen_width / 2 - enemy_width / 2 
    enemy_Y_pos = screen_height / 2 - enemy_height / 2   
    enemy_to_X = 0
    enemy_to_Y = 0
    enemy_speed = 0

def Draw_object():
    global background
    global background_X_pos
    global background_Y_pos
    global character
    global character_X_pos
    global character_Y_pos
    global enemy
    global enemy_X_pos
    global enemy_Y_pos

    screen.blit(background, (background_X_pos, background_Y_pos))
    screen.blit(character, (character_X_pos, character_Y_pos))
    screen.blit(enemy, (enemy_X_pos, enemy_Y_pos))

def Move_Enemy():
    global enemy_direction_decision
    global enemy_to_X
    global enemy_to_Y
    global enemy_speed
    global begin

    enemy_speed = playtime * 0.0001

    if enemy_direction_decision == 30:
        enemy_to_X = random.uniform((-1 * enemy_speed), enemy_speed)
        enemy_to_Y = random.uniform((-1 * enemy_speed), enemy_speed)
        enemy_direction_decision = 0
    else:
        enemy_direction_decision += 1

def Move_object():
    global dt
    global character_to_X
    global character_to_Y
    global character_X_pos
    global character_Y_pos
    global enemy_to_X
    global enemy_to_Y
    global enemy_X_pos
    global enemy_Y_pos

    character_X_pos += character_to_X * dt
    character_Y_pos += character_to_Y * dt

    enemy_X_pos += enemy_to_X * dt
    enemy_Y_pos += enemy_to_Y * dt

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
            character_to_X -= speed
        elif event.key == pygame.K_d: 
            character_to_X += speed
        elif event.key == pygame.K_w: 
            character_to_Y -= speed
        elif event.key == pygame.K_s: 
            character_to_Y += speed

    if event.type == pygame.KEYUP: 
        if event.key == pygame.K_a or event.key == pygame.K_d:
            character_to_X = 0
        elif event.key == pygame.K_w or event.key == pygame.K_s:
            character_to_Y = 0


def Ask_FPS():
    global fps
    temp = input("프레임을 몇으로 설정하시겠습니까? : ")
    fps = int(temp)

def Ask_level():
    global speed
    global level

    temp = input("난이도를 몇으로 설정하시겠습니까? (쉬움/보통/어려움/하드코어) : ")
    if temp == '쉬움':
        speed = 1
        level = 1
    elif temp == '보통':
        speed = 0.5
        level = 2
    elif temp == '어려움':
        speed = 0.3
        level = 3
    elif temp == '하드코어':
        speed = 0.15
        level = 4
    else:
        print("오류 발생 (error code : 001)")
        print("난이도를 잘못 설정하셨습니다. 다시 입력해주세요 : ")
        Ask_level()

def Wall_Collision():
    global screen_width
    global screen_height
    global character_X_pos
    global character_Y_pos
    global character_width
    global character_height
    global enemy_X_pos
    global enemy_Y_pos
    global enemy_width
    global enemy_height
    
    if character_X_pos < 0:
        character_X_pos = 0
    elif character_X_pos > screen_width - character_width:
        character_X_pos = screen_width - character_width

    if character_Y_pos < 0:
        character_Y_pos = 0
    elif character_Y_pos > screen_height - character_height:
        character_Y_pos = screen_height - character_height

    if enemy_X_pos < 0:
        enemy_X_pos = 0
    elif enemy_X_pos > screen_width - enemy_width:
        enemy_X_pos = screen_width - enemy_width

    if enemy_Y_pos < 0:
        enemy_Y_pos = 0
    elif enemy_Y_pos > screen_height - enemy_height:
        enemy_Y_pos = screen_height - enemy_height
    
    if enemy_X_pos < -100:
        enemy_X_pos = 0
    elif enemy_X_pos > 700:
        enemy_X_pos = 0
    elif enemy_Y_pos < -100:
        enemy_Y_pos = 0
    elif enemy_Y_pos > 700:
        enemy_Y_pos = 0

def Setup_Leave_KeyboardEvent():
    global running
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_l:
            running = False

def Update_Rect():
    global character_rect
    global character_X_pos
    global character_Y_pos
    global enemy_rect
    global enemy_X_pos
    global enemy_Y_pos

    character_rect = character.get_rect()
    character_rect.left = character_X_pos
    character_rect.top = character_Y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_X_pos
    enemy_rect.top = enemy_Y_pos
    
def Enemy_Collision():
    global character_rect
    global enemy_rect
    global running
    
    if character_rect.colliderect(enemy_rect):
        print("Game over!")
        running = False

def Estimate_score():
    global playtime
    global score

    score = playtime * 0.01
    score = round(score)

def Check_Playtime():
    global begin
    global end
    global playtime
    
    end = time.time()
    temp2 = end - begin
    playtime += temp2

def Setup_AllObject():
    Setup_Background()
    Setup_Character()
    Setup_Enemy()

def KeyboardEvent():
    Perceive_KeyboardEvent()
    Setup_Leave_KeyboardEvent()

def Ask():
    Ask_FPS()
    Ask_level()











pygame.init()

Setup_variable()
Ask()
Setup_Screen(600, 600)
Setup_AllObject()
Setup_Character_KeyboardEvent()
pygame.display.set_caption("Avoid The Tagger")

# main loop

running = True

begin = time.time()

while running:
    dt = clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        KeyboardEvent()
    
    Check_Playtime()
    Update_Rect()
    Move_object()
    Draw_object()
    Move_Enemy()
    Wall_Collision()
    Enemy_Collision()
    pygame.display.update()


Estimate_score()
print("당신의 점수는 {0} 점 입니다.".format(score))
input("")
pygame.quit()
