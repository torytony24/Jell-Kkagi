import pygame
from settings import *
from math import *
from copy import copy
from sound import *

def drawGameover(screen, images):
    gameOver = images[3]
    screen.blit(gameOver, (-40, -100))

def drawWinState(screen, images, stones, time):
    pinkWin = images[9]
    purpleWin = images[10]
    pinkWinDance = images[11]
    purpleWinDance = images[12]
    tie = images[13]

    if len(stones) == 0:
        screen.blit(tie, (250, HEIGHT//2 + 150))
        size = pinkWinDance.get_size()
        pinkWinDance = pygame.transform.scale(pinkWinDance, (size[0]*0.8, size[1]*0.8 + 20*sin(time/3)))
        screen.blit(pinkWinDance, (WIDTH//2 - 150 - 200, HEIGHT//2 - 150 - 10*sin(time/3)))
        size = purpleWinDance.get_size()
        purpleWinDance = pygame.transform.scale(purpleWinDance, (size[0]*0.8, size[1]*0.8 + 20*sin(time/3)))
        screen.blit(purpleWinDance, (WIDTH//2 - 150 + 200, HEIGHT//2 - 150 - 10*sin(time/3)))
    else:
        cnt1, cnt2 = 0, 0
        for stone in stones:
            if stone.player == 'player1':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 > 0 and cnt2 == 0:
            screen.blit(pinkWin, (100, HEIGHT//2 + 150))
            size = pinkWinDance.get_size()
            pinkWinDance = pygame.transform.scale(pinkWinDance, (size[0]*0.8, size[1]*0.8 + 20*sin(time/3)))
            screen.blit(pinkWinDance, (WIDTH//2 - 150, HEIGHT//2 - 150 - 10*sin(time/3)))
        if cnt1 == 0 and cnt2 > 0:
            screen.blit(purpleWin, (50, HEIGHT//2 + 150))
            size = purpleWinDance.get_size()
            purpleWinDance = pygame.transform.scale(purpleWinDance, (size[0]*0.8, size[1]*0.8 + 20*sin(time/3)))
            screen.blit(purpleWinDance, (WIDTH//2 - 150, HEIGHT//2 - 150 - 10*sin(time/3)))


def playAgain(screen, mouse, gameState, button, images):
    replay = images[14]
    screen.blit(replay, (WIDTH - 300, HEIGHT//2 + 50))

    mouseX, mouseY = mouse.get_pos()
    mouseClick = mouse.get_pressed()[0]

    button.draw(screen)
    button.update(mouse)
    if button.x - button.width//2 < mouseX < button.x + button.width//2 and button.y - button.height//2 < mouseY < button.y + button.height//2 and mouseClick:
        effectChannel.play(bounce)
        gameState[0] = button.command

    