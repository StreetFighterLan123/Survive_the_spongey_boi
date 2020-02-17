import pygame
import random
import math
import time



pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Survive the Spongey Boi")

#Sounds
game_over_sound = pygame.mixer.Sound("Game_Over.wav")
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

#Positions of the text.
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score: " + str(score_value//1), True, (0,0,0))
    screen.blit(score, (x,y))


#Player
playerImg = pygame.image.load('monster.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#Spongebob
enemyImg = pygame.image.load('sponge.png')
enemyX = random.randint(0,735)
enemyY = random.randint(10,400)
enemyX_change = 0
enemyY_change = 0

#Coin
coinImg = pygame.image.load('coin.png')
coinX = random.randint(0,735)
coinY = random.randint(0,535)


#Font for Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

def coin(x,y):
    screen.blit(coinImg, (x,y))



def isCollision(enemyX, enemyY, playerX, playerY):
    #Distance formula in Python
    distance = math.sqrt((math.pow(enemyX - playerX,2)) + (math.pow(enemyY - playerY,2))) 
    if distance < 27:
        return True
    else: 
        return False

def coin_collision(coinX, coinY, playerX, playerY):
    distance = math.sqrt((math.pow(coinX - playerX,2)) + (math.pow(coinY - playerY,2))) 
    if distance < 27:
        return True
    else: 
        return False

    
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (200,250))

#Game loop
running = True

while running:
    screen.fill((255,255,204))
    #Do the for loop here.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Do the keydown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_UP:
                playerY_change = -2
            if event.key == pygame.K_DOWN:
                playerY_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
        

    playerX += playerX_change
    playerY += playerY_change
    
    enemyX += enemyX_change
    enemyY += enemyY_change
    #Boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY > 536:
        playerY = 536
        
    if enemyX <= 0:
        enemyX = 0
    elif enemyX > 736:
        enemyX = 736
    if enemyY <= 0:
        enemyY = 0
    elif enemyY > 536:
        enemyY = 536

    if isCollision(enemyX, enemyY, playerX, playerY):
        game_over_text()
        playerX = 10000
        enemyX = 10000
        pygame.mixer.Sound.play(game_over_sound)
        time.sleep(3.5)
        break
    #CHANGE THIS LATER
    enemyX_change = random.randint(-30,30)
    enemyY_change = random.randint(-30,30)
    
    score_value += 0.003
    #score_value = score_value//1
    show_score(textX, textY)
    coin(coinX, coinY)
    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()
