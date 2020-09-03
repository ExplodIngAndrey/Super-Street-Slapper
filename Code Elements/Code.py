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

# Title and Icon
pygame.display.set_caption('Super Street Slapper')
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Player.png')
playerX = 0
playerY = 380
playerXChange = 0

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 20
scoreY = 20

def player(x, y):
    screen.blit(playerImg, (x, y))

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def jump():
  for x in range(1,20):
    time.sleep(0.05)
    playerY -= 0.1
  for x in range(1,20):
    time.sleep(0.01)
    playerY += 0.1

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
            if event.key == pygame.K_SPACE:
                jump()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a or event.key == pygame.K_SPACE:
                playerXChange = 0
    
    playerX += playerXChange
    
    # Creates Movement Bounderies
    if playerX <= 0:
        playerX = 0
    elif playerX >= 600:
        playerX = 600

    player(playerX, playerY) # Shows Player
    show_score(scoreX, scoreY) # Writes score
    pygame.display.update() # Updates Screen
