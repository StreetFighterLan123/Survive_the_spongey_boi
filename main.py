import pygame
import random
import math
import time



pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Survive the Spongey Boi")

#Sounds

game_over_sound = pygame.mixer.Sound("Game_Over.wav")
#MUSIC - Background
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound("coin_sound.wav")

#Dead or not variable
dead = False
not_revived = True

#Score
coins_collected = 0
font = pygame.font.Font('freesansbold.ttf', 32)
#coinfont = pygame.font.Font('freesansbold.ttf', 16)
#Positions of the text.
coin_textX = 10
coin_textY = 10

#ONCE VARIABLES
five_once = True
ten_once = True
fifteen_once = True
twenty_once = True
#twentyfive_once is going to make is so that you "beat" the game.
twentyfive_once = True


def show_coin_score(x,y):
    coins_text = font.render("Coins: " + str(coins_collected), True, (0,0,0))
    screen.blit(coins_text, (x,y))

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
enemyX_change_origin = 5
enemyY_change_origin = 5

#Coin
coinImg = pygame.image.load('coin.png')
coinX = random.randint(0,735)
coinY = random.randint(0,535)

#Button when you die
#buttonImg = pygame.image.load('')
#buttonX = 
#buttonY = 

#Font for Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
#Font for You Win
win_font = pygame.font.Font('freesansbold.ttf', 64)

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

def coin(x,y):
    screen.blit(coinImg, (x,y))

#def button(x,y):
    #screen.blit(buttonImg(x,y))
    #Make it so that when you click the button, not_revived is false 

def isCollision(enemyX, enemyY, playerX, playerY):
    #Distance formula in Python
    distance = math.sqrt((math.pow(enemyX - playerX,2)) + (math.pow(enemyY - playerY,2))) 
    if distance < 27:
        return True
    else: 
        return False

def coin_collision(coinX, coinY, playerX, playerY):
    distance = math.sqrt((math.pow(coinX - playerX,2)) + (math.pow(coinY - playerY,2))) 
    if distance < 32:
        return True
    else: 
        return False

    
def game_over_text():
    if not_revived:
        over_text = over_font.render("GAME OVER", True, (0, 0, 0))
        screen.blit(over_text, (200,250))

def win_text():
    you_win_text = win_font.render("You win! For now...", True, (0,0,0))
    screen.blit(you_win_text, (200,250))

#Game loop
running = True

while running:
    screen.fill((255,255,206))
    #Do the for loop here.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Do the keydown
        #CHANGE THIS ACCORDING TO THAT GUY ON STACK OVERFLOW BECAUSE THIS METHOD ISN'T GOOD
    keys = pygame.key.get_pressed()
    playerX_change, playerY_change = 0, 0
    if keys[pygame.K_LEFT]:
        playerX_change -= 2
    if keys[pygame.K_RIGHT]:
        playerX_change += 2
    if keys[pygame.K_UP]:
        playerY_change -= 2
    if keys[pygame.K_DOWN]:
        playerY_change += 2
        

    playerX += playerX_change
    playerY += playerY_change
    
    #enemyX += enemyX_change
   #enemyY += enemyY_change
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
        dead = True
        show_coin_score(coin_textX, coin_textY)
        game_over_text()
        playerX = 100000000
        enemyX = 100000000
        pygame.display.update()
        pygame.mixer.Sound.play(game_over_sound)
        time.sleep(3.5)
        break
    if coin_collision(coinX, coinY, playerX, playerY):
        coins_collected += 1
        #time.sleep(0.00001)
        coinX = random.randint(0,735)
        coinY = random.randint(0,535)
        pygame.mixer.Sound.play(coin_sound)

    #This is when you first get 5, etc.
    if coins_collected >= 5 and five_once == True:
        enemyX_change_origin += 5
        enemyY_change_origin += 5
        five_once = False
    if coins_collected >= 10 and ten_once == True:
        enemyX_change_origin += 5
        enemyY_change_origin += 5
        ten_once = False
    if coins_collected >= 15 and fifteen_once == True:
        enemyX_change_origin += 5
        enemyY_change_origin += 5
        fifteen_once = False
    if coins_collected >= 20 and twenty_once == True:
        enemyX_change_origin += 5
        enemyY_change_origin += 5
        twenty_once = False
    #After 25 something new happens or you "beat" the game
    if coins_collected >= 25 and twentyfive_once == True:
        win_text()
        playerX = 10000
        enemyX = 10000
        pygame.display.update()
        twentyfive_once = False
        time.sleep(3.5)
        break



    enemyX_change = random.randint(-(abs(enemyX_change_origin)), abs((enemyX_change_origin)))
    enemyY_change = random.randint(-(abs(enemyY_change_origin)), (abs(enemyY_change_origin)))

    #score_value = score_value//1
    enemyX += enemyX_change
    enemyY += enemyY_change
    show_coin_score(coin_textX, coin_textY)
    coin(coinX, coinY)
    enemy(enemyX, enemyY)
    player(playerX, playerY)
    time.sleep(0.001)
    pygame.display.update()
