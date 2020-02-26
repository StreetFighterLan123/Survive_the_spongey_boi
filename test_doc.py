import pygame
import time
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Test BETA FEATURES")

win_font = pygame.font.Font('freesansbold.ttf', 64)

def win_text():
    you_win_text = win_font.render("You win! For now...", True, (0,0,0))
    screen.blit(you_win_text, (115,250))

running = True

while running:
    screen.fill((255,255,206))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win_text()
    time.sleep(0.001)
    pygame.display.update()
