import pygame
from conv3D import *
from settings import *
from objects import calcDist
from sound import *



def drawBoard(screen, mouse):
    font = pygame.font.SysFont("consolas", 20)
    tip1 = font.render("RIGHT drag : viewpoint", True, (0,0,0))
    tip2 = font.render("LEFT drag : shoots stone", True, (0,0,0))

    screen.blit(tip1, (50, HEIGHT - 50))
    screen.blit(tip2, (50, HEIGHT - 80))

    # Right click -> board control
    mouseRightClick = mouse.get_pressed()[2]
    if not rightMousePressed[0] and mouseRightClick:
        originPos[0] = mouse.get_pos()
        rightMousePressed[0] = True
    elif rightMousePressed[0] and mouseRightClick:
        currentPos = mouse.get_pos()
        if currentPos[1] >= HEIGHT//2:
            theta[0] += (originPos[0][0] - currentPos[0])/1000
        else:
            theta[0] += -(originPos[0][0] - currentPos[0])/1000
        h[0] += -(originPos[0][1] - currentPos[1])*0.2
        originPos[0] = currentPos
    elif rightMousePressed[0] and not mouseRightClick:
        rightMousePressed[0] = False

    # Draw board
    quard1 = conv3D(LENGTH//2,LENGTH//2)
    quard2 = conv3D(-LENGTH//2,LENGTH//2)
    quard3 = conv3D(-LENGTH//2,-LENGTH//2)
    quard4 = conv3D(LENGTH//2,-LENGTH//2)

    pygame.draw.polygon(screen, (248,195,117), (quard1, quard2, quard3, quard4))

    N = 10
    for i in range(1,N):
        pygame.draw.line(screen, (223,163,103), (quard1[0]*i/N + quard4[0]*(N-i)/N, quard1[1]*i/N + quard4[1]*(N-i)/N), (quard2[0]*i/N + quard3[0]*(N-i)/N, quard2[1]*i/N + quard3[1]*(N-i)/N), 5)
        pygame.draw.line(screen, (223,163,103), (quard1[0]*i/N + quard2[0]*(N-i)/N, quard1[1]*i/N + quard2[1]*(N-i)/N), (quard4[0]*i/N + quard3[0]*(N-i)/N, quard4[1]*i/N + quard3[1]*(N-i)/N), 5)

    # relative line
    pygame.draw.line(screen, (135,83,61), quard1, quard2, 5)
    pygame.draw.line(screen, (135,83,61), quard2, quard3, 5)
    pygame.draw.line(screen, (135,83,61), quard3, quard4, 5)
    pygame.draw.line(screen, (135,83,61), quard4, quard1, 5)


def drawStone(screen, stones):
    for stone in stones:
        stone.draw(screen)
        stone.update(stones)
        if stone.outOfBoard():
            # animation for stone //////// here ////////
            stones.remove(stone)

def moveStone(screen, mouse, stones):
    # Left click -> stone control
    mouseLeftClick = mouse.get_pressed()[0]
    if not leftMousePressed[0] and mouseLeftClick:
        
        leftClickedPos = mouse.get_pos()
        for stone in stones:
            cenX, cenY = conv3D(stone.x, stone.y)
            particle = stone.particleList[0]
            edgeX, edgeY = conv3D(particle.x, particle.y)
            if stone.player == playerTurn[0] and calcDist(leftClickedPos[0], leftClickedPos[1], cenX, cenY) < calcDist(cenX, cenY, edgeX, edgeY):
                targetStone[0] = stone
        leftMousePressed[0] = True
    elif leftMousePressed[0] and mouseLeftClick:
        draggedPos[0] = mouse.get_pos()
        if targetStone[0] != None:
            targetX, targetY = conv3D(targetStone[0].x,targetStone[0].y)
            mouseX, mouseY = draggedPos[0]
            endX, endY = 2*targetX-mouseX, 2*targetY-mouseY
            drawTargetLine(screen, targetX, targetY, endX, endY)


    elif leftMousePressed[0] and not mouseLeftClick:
        if targetStone[0] != None:
            effectChannel.play(bounce)
            targetStone[0].move(draggedPos[0])
            movingStone[0] = targetStone[0]
            targetStone[0] = None
        leftMousePressed[0] = False

def drawTargetLine(screen, targetX, targetY, endX, endY):
    N = 20
    for i in range(N):
        if i%2 == 1:
            pygame.draw.line(screen, (112,190,220), (targetX*i/N + endX*(N-i)/N, targetY*i/N + endY*(N-i)/N), (targetX*(i+1)/N + endX*(N-(i+1))/N, targetY*(i+1)/N + endY*(N-(i+1))/N), 5)

def drawStoneState(screen, stones, images):
    pinkWinDance = images[4]
    size = pinkWinDance.get_size()
    pinkWinDance = pygame.transform.scale(pinkWinDance, (size[0]*0.25, size[1]*0.25))
    screen.blit(pinkWinDance, (20,100))

    purpleWinDance = images[5]
    size = purpleWinDance.get_size()
    purpleWinDance = pygame.transform.scale(purpleWinDance, (size[0]*0.25, size[1]*0.25))
    screen.blit(purpleWinDance, (WIDTH//2 + 450, 100))

    pinkTitle = images[6]
    size = pinkTitle.get_size()
    pinkTitle = pygame.transform.scale(pinkTitle, (size[0]*0.6, size[1]*0.6))
    screen.blit(pinkTitle, (-20, -20))

    purpleTitle = images[7]
    size = purpleTitle.get_size()
    purpleTitle = pygame.transform.scale(purpleTitle, (size[0]*0.6, size[1]*0.6))
    screen.blit(purpleTitle, (WIDTH//2 + 230, -20))

    arrowLeft = images[15]
    size = arrowLeft.get_size()
    arrowLeft = pygame.transform.scale(arrowLeft, (size[0]*0.5, size[1]*0.5))

    arrowRight = images[16]
    size = arrowRight.get_size()
    arrowRight = pygame.transform.scale(arrowRight, (size[0]*0.5, size[1]*0.5))

    cnt1, cnt2 = 0, 0
    for stone in stones:
        if stone.player == 'player1':
            cnt1 += 1
        else:
            cnt2 += 1

    for i in range(1, 4):
        if cnt1 >= i:
            pygame.draw.circle(screen, (245,114,239), (200 + 50*(i-1), 150), 20)
            pygame.draw.circle(screen, (242,72,235), (200 + 50*(i-1), 150), 15)
        if cnt1 < i:
            pygame.draw.circle(screen, (129,87,166), (200 + 50*(i-1), 150), 20)
            pygame.draw.circle(screen, (126,65,164), (200 + 50*(i-1), 150), 15)
        if cnt2 >= i:
            pygame.draw.circle(screen, (201,113,245), (1000 - 50*(i-1), 150), 20)
            pygame.draw.circle(screen, (185,71,242), (1000 - 50*(i-1), 150), 15)
        if cnt2 < i:
            pygame.draw.circle(screen, (106,86,168), (1000 - 50*(i-1), 150), 20)
            pygame.draw.circle(screen, (97,64,166), (1000 - 50*(i-1), 150), 15)

    if playerTurn[0] == 'player1':
        screen.blit(arrowLeft, (250, -25))
    else:
        screen.blit(arrowRight, (WIDTH//2 + 140, -25))
