# Modules
import pygame


# Files
from drawBackground import *
from startMenu import *
from play import *
from settings import *
from objects import *
from playDone import *
from moveAI import *
from sound import *


# Game initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Jell Kkagi 3D")


# Load background images
scroll = 0
bgImages = []
for i in range(1, 9):
    bgImage = pygame.image.load(f"resources/background_images/layer{i}.png").convert_alpha()
    bgImages.append(bgImage)


# Get images
title = pygame.image.load('resources/images/title.png').convert_alpha()
play = pygame.image.load('resources/images/play.png').convert_alpha()
practice = pygame.image.load('resources/images/practice.png').convert_alpha()
gameOver = pygame.image.load('resources/images/gameover.png').convert_alpha()
pinkTeam = pygame.image.load('resources/images/pinkteam.png').convert_alpha()
size = pinkTeam.get_size()
pinkTeam = pygame.transform.scale(pinkTeam, (size[0]*0.8, size[1]*0.8))
purpleTeam = pygame.image.load('resources/images/purpleteam.png').convert_alpha()
size = purpleTeam.get_size()
purpleTeam = pygame.transform.scale(purpleTeam, (size[0]*0.8, size[1]*0.8))
pinkTitle = pygame.image.load('resources/images/pinktitle.png').convert_alpha()
size = pinkTitle.get_size()
pinkTitle = pygame.transform.scale(pinkTitle, (size[0]*0.8, size[1]*0.8))
purpleTitle = pygame.image.load('resources/images/purpletitle.png').convert_alpha()
size = purpleTitle.get_size()
purpleTitle = pygame.transform.scale(purpleTitle, (size[0]*0.8, size[1]*0.8))
back = pygame.image.load('resources/images/back.png').convert_alpha()
pinkWin = pygame.image.load('resources/images/pinkwin.png').convert_alpha()
purpleWin = pygame.image.load('resources/images/purplewin.png').convert_alpha()
pinkWinDance = pygame.image.load('resources/images/pinkwindance.png').convert_alpha()
purpleWinDance = pygame.image.load('resources/images/purplewindance.png').convert_alpha()
tie = pygame.image.load('resources/images/tie.png').convert_alpha()
replay = pygame.image.load('resources/images/replay.png').convert_alpha()
arrowLeft = pygame.image.load('resources/images/arrowleft.png').convert_alpha()
arrowRight = pygame.image.load('resources/images/arrowright.png').convert_alpha()
you = pygame.image.load('resources/images/you.png').convert_alpha()
size = you.get_size()
you = pygame.transform.scale(you, (size[0]*0.8, size[1]*0.8))
ai = pygame.image.load('resources/images/ai.png').convert_alpha()
size = ai.get_size()
ai = pygame.transform.scale(ai, (size[0]*0.8, size[1]*0.8))
images = [title, play, practice, gameOver, pinkTeam, purpleTeam, pinkTitle, purpleTitle, back, pinkWin, purpleWin, pinkWinDance, purpleWinDance, tie, replay, arrowLeft, arrowRight, you, ai]
#          0      1       2         3         4          5            6            7       8      9         10         11             12          13   14       15           16        17  18

# Creat components
playButtonJelly = ButtonJelly(WIDTH//2, HEIGHT//2, 220, 120, 'chooseTeam')
practiceButtonJelly = ButtonJelly(WIDTH//2, HEIGHT//2 + 180, 380, 120, 'practice')
buttonJellys_start = [playButtonJelly, practiceButtonJelly]
nextButtonJelly = ButtonJelly(WIDTH- 160, HEIGHT - 115, 230, 120, 'play')
backButtonJelly = ButtonJelly(160, HEIGHT - 115, 230, 120, 'startMenu')
buttonJellys_team = [nextButtonJelly, backButtonJelly]
replayButtonJelly = ButtonJelly(WIDTH - 130, HEIGHT - 295, 220, 100, 'chooseTeam')
aiButtonJelly = ButtonJelly(WIDTH- 160, HEIGHT - 115, 230, 120, 'playAI')
backButtonJelly = ButtonJelly(160, HEIGHT - 115, 230, 120, 'startMenu')
buttonJellys_ai = [aiButtonJelly, backButtonJelly]

# Main loop
running = True
gameState = ['startMenu']
time = 0
timeStamp = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameState[0] = 'startMenu'

    mouse = pygame.mouse

    # draw background
    drawBackground(screen, time, bgImages, gameState)
    time += 0.5

    if gameState[0] == 'startMenu':
        # Title, Play button, Practice button
        startMenu(screen, mouse, time, buttonJellys_start, images, gameState)

    elif gameState[0] == 'chooseTeam':
        playerTurn[0] = 'player1'
        player1Left = Stone(LENGTH*0.3, -LENGTH*0.25, LENGTH*0.05, 'player1', False)
        player1Middle = Stone(LENGTH*0.3, 0, LENGTH*0.06, 'player1', True)
        player1Right = Stone(LENGTH*0.3, LENGTH*0.25, LENGTH*0.05, 'player1', False)
        player2Left = Stone(-LENGTH*0.3, -LENGTH*0.25, LENGTH*0.05, 'player2', False)
        player2Middle = Stone(-LENGTH*0.3, 0, LENGTH*0.06, 'player2', True)
        player2Right = Stone(-LENGTH*0.3, LENGTH*0.25, LENGTH*0.05, 'player2', False)
        stones = [player1Left, player1Middle, player1Right, player2Left, player2Middle, player2Right]
        h[0] = 150
        r[0] = 100
        theta[0] = 0.05
        timeStamp = 0
        chooseTeam(screen, mouse, time, images, buttonJellys_team, gameState)


    elif gameState[0] == 'practice':
        playerTurn[0] = 'player1'
        player1Left = Stone(LENGTH*0.3, -LENGTH*0.25, LENGTH*0.05, 'player1', False)
        player1Middle = Stone(LENGTH*0.3, 0, LENGTH*0.06, 'player1', True)
        player1Right = Stone(LENGTH*0.3, LENGTH*0.25, LENGTH*0.05, 'player1', False)
        player2Left = Stone(-LENGTH*0.3, -LENGTH*0.25, LENGTH*0.05, 'player2', False)
        player2Middle = Stone(-LENGTH*0.3, 0, LENGTH*0.06, 'player2', True)
        player2Right = Stone(-LENGTH*0.3, LENGTH*0.25, LENGTH*0.05, 'player2', False)
        stones = [player1Left, player1Middle, player1Right, player2Left, player2Middle, player2Right]
        h[0] = 150
        r[0] = 100
        theta[0] = 0.05
        timeStamp = 0

        chooseTeamAI(screen, mouse, time, images, buttonJellys_ai, gameState)

    elif gameState[0] == 'play':
        drawBoard(screen, mouse)
        drawStone(screen, stones)
        if not isMoving[0]:
            moveStone(screen, mouse, stones)
        drawStoneState(screen, stones, images)
        if movingStone[0] != None:
            particle = movingStone[0].particleList[0]
            if particle.vx**2 + particle.vy**2 > 10:
                isMoving[0] = True
            if isMoving[0] and particle.vx**2 + particle.vy**2 < 0.1 or movingStone[0] not in stones:
                movingStone[0] = None
                isMoving[0] = False
                # Turn player
                timeStamp = time
                gameState[0] = 'turn'
                
        cnt1, cnt2 = 0, 0
        for stone in stones:
            if stone.player == 'player1':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 == 0 or cnt2 == 0:
            timeStamp = time
            gameState[0] = 'playDone'


    elif gameState[0] == 'turn':
        drawBoard(screen, mouse)
        drawStone(screen, stones)
        drawStoneState(screen, stones, images)
        if time - timeStamp > 20:
            if turn180[0] < 5:
                turn180[0] += 1
                theta[0] += pi/60
            elif 5 <= turn180[0] < 15:
                turn180[0] += 1
                theta[0] += pi/60*5
            elif 15 <= turn180[0] < 20:
                turn180[0] += 1
                theta[0] += pi/60
            else:
                turn180[0] = 0
                if playerTurn[0] == 'player1':
                        playerTurn[0] = 'player2'
                elif playerTurn[0] == 'player2':
                    playerTurn[0] = 'player1'
                gameState[0] = 'play'

    elif gameState[0] == 'playDone':
        drawBoard(screen, mouse)
        drawStone(screen, stones)
        drawStoneState(screen, stones, images)
        if time - timeStamp >= 30:
            subChannel_signal()
            drawGameover(screen, images)
            drawWinState(screen, images, stones, time)
            playAgain(screen, mouse, gameState, replayButtonJelly, images)
        elif time - timeStamp >= 15:
            drawGameover(screen, images)

    elif gameState[0] == 'playAI':
        drawBoard(screen, mouse)
        drawStone(screen, stones)
        if not isMoving[0]:
            moveStone(screen, mouse, stones)
        drawStoneState(screen, stones, images)
        if movingStone[0] != None:
            particle = movingStone[0].particleList[0]
            if particle.vx**2 + particle.vy**2 > 10:
                isMoving[0] = True
            if isMoving[0] and particle.vx**2 + particle.vy**2 < 0.1 or movingStone[0] not in stones:
                movingStone[0] = None
                isMoving[0] = False
                # Turn player

                timeStamp = time
                playerTurn[0] = 'player2'
                gameState[0] = 'turnAI'

        cnt1, cnt2 = 0, 0
        for stone in stones:
            if stone.player == 'player1':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 == 0 or cnt2 == 0:
            timeStamp = time
            gameState[0] = 'playDone'
                

    elif gameState[0] == 'turnAI':
        drawBoard(screen, mouse)
        drawStone(screen, stones)
        drawStoneState(screen, stones, images)

        cnt1, cnt2 = 0, 0
        for stone in stones:
            if stone.player == 'player1':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 == 0 or cnt2 == 0:
            timeStamp = time
            gameState[0] = 'playDone'

        moveAI(screen, stones, gameState)

        playerTurn[0] = 'player1'
        gameState[0] = 'playAI'

    pygame.display.flip()

pygame.quit()

