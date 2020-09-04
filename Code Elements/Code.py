import pygame
from pygame import mixer
import time

# Initialize Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('Background.png')

# Background Sound
mixer.music.load('BackgroundMusic.wav')
mixer.music.play(-1)

# ID Sounds
coinSound = mixer.Sound('Coin.wav')
fallingSound = mixer.Sound('Falling.wav')
jumpSound = mixer.Sound('Jump.wav')
menuSelectSound = mixer.Sound('MenuSelect.wav')
pauseSound = mixer.Sound('Pause.wav')
unpauseSound = mixer.Sound('Unpause.wav')

# Title and Icon
pygame.display.set_caption('Street Fighter')
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Player.png')
playerX = 0
playerY = 380
playerXChange = 0
vel = 5
height = 100
isJump = False
jumpCount = 10

# Enemy
enemyImg = pygame.image.load('Enemy.png')
enemyX = 600
enemyY = 400
enemyXChange = 0

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 20
scoreY = 20

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Game Loop
running = True
while running:
    screen.blit(background, (0, 0))
    # Check for Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerXChange = 1
            if event.key == pygame.K_a:
                playerXChange = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                playerXChange = 0

    playerX += playerXChange

    # Creates Movement Bounderies
    if playerX <= 0:
        playerX = 0
    if playerX >= 770:
        playerX = 770

    keys = pygame.key.get_pressed()

    if not(isJump):
        if keys[pygame.K_SPACE]:
            jumpSound.play()
            isJump = True
    else:
        if jumpCount >= -10:
            playerY -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    player(playerX, playerY)  # Shows Player
    enemy(enemyX, enemyY) # Shows Enemy
    show_score(scoreX, scoreY)  # Writes score
    pygame.display.update()  # Updates Screen
