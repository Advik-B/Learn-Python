import math
import random
import os
import pygame
from pygame import mixer
from itertools import cycle

# Intialize the pygame
pygame.init()

bullets_used = 0
# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load(r'assets\background.png')

# Sound
mixer.music.load(r"assets\sounds\background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
pygame.display.fullscreen = True
# icon = pygame.image.load(r'assets\spaceship512.png')
# pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(r'assets\heros\4.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
parent_dir = os.getcwd()
enemy_folder = os.path.join(parent_dir , 'assets' , 'enemys')
enemy_list = []

for file in os.listdir(enemy_folder):
    enemy_list.append(os.path.join(enemy_folder , file))

enemyImgs = cycle(sorted(enemy_list))
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(next(enemyImgs)))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(.4)
    enemyY_change.append(40)

bullets_have = num_of_enemies + 5

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load(r'assets\bullets\bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 35:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.6
            if event.key == pygame.K_RIGHT:
                playerX_change = .6
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound(r"assets\sounds\laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    
                    fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = .4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -.4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound(r"assets\sounds\explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            bullets_have += 10
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        bullets_used += 1
        if bullets_used == 10:
            score_value -= 1


    if bullet_state == "fire":
        # if bullets_have > 0:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        bullets_have -= 1

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
