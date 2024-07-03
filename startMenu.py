import pygame
from math import *
from settings import *
from sound import *

def startMenu(screen, mouse, time, buttonJellys_start, images, gameState):
        
        mouseX, mouseY = mouse.get_pos()
        mouseClick = mouse.get_pressed()[0]

        #create buttons on screen & click command
        for button in buttonJellys_start:
            button.draw(screen)
            button.update(mouse)
            if button.x - button.width//2 < mouseX < button.x + button.width//2 and button.y - button.height//2 < mouseY < button.y + button.height//2 and mouseClick:
                effectChannel.play(bounce)
                gameState[0] = button.command

        # show images on screen
        title = images[0]
        titleWidth, titleHeight = title.get_size()
        screen.blit(title, (WIDTH//2 - titleWidth//2, -75 + 8*sin(time/5)))

        play = images[1]
        screen.blit(play, (WIDTH//2 - 185, 310))

        practice = images[2]
        screen.blit(practice, (WIDTH//2 - 260, 495))

def chooseTeam(screen, mouse, time, images, buttonJellys_team, gameState):
    pinkTeam = images[4]
    screen.blit(pinkTeam, (40, 280 + 8*sin(time/10)))
    purpleTeam = images[5]
    screen.blit(purpleTeam, (WIDTH//2 + 20, 280 + 8*sin(time/10)))
    pinkTitle = images[6]
    screen.blit(pinkTitle, (0 - 10, 0))
    purpleTitle = images[7]
    screen.blit(purpleTitle, (WIDTH//2 - 30, 0))
    back = images[8]
    screen.blit(back, (-30, HEIGHT//2 + 200))
    play = images[1]
    screen.blit(play, (WIDTH - 340, HEIGHT//2 + 200))

    mouseX, mouseY = mouse.get_pos()
    mouseClick = mouse.get_pressed()[0]
    
    for button in buttonJellys_team:
        button.draw(screen)
        button.update(mouse)
        if button.x - button.width//2 < mouseX < button.x + button.width//2 and button.y - button.height//2 < mouseY < button.y + button.height//2 and mouseClick:
            effectChannel.play(bounce)
            gameState[0] = button.command

def chooseTeamAI(screen, mouse, time, images, buttonJellys_ai, gameState):
    pinkTeam = images[4]
    screen.blit(pinkTeam, (40, 280 + 8*sin(time/10)))
    purpleTeam = images[5]
    screen.blit(purpleTeam, (WIDTH//2 + 20, 280 + 8*sin(time/10)))
    pinkTitle = images[6]
    screen.blit(pinkTitle, (0 - 10, 0))
    purpleTitle = images[7]
    screen.blit(purpleTitle, (WIDTH//2 - 30, 0))
    back = images[8]
    screen.blit(back, (-30, HEIGHT//2 + 200))
    play = images[1]
    screen.blit(play, (WIDTH - 340, HEIGHT//2 + 200))

    you = images[17]
    screen.blit(you, (200, 150))
    ai = images[18]
    screen.blit(ai, (WIDTH//2 - 30 + 100, 150))


    mouseX, mouseY = mouse.get_pos()
    mouseClick = mouse.get_pressed()[0]
    
    for button in buttonJellys_ai:
        button.draw(screen)
        button.update(mouse)
        if button.x - button.width//2 < mouseX < button.x + button.width//2 and button.y - button.height//2 < mouseY < button.y + button.height//2 and mouseClick:
            effectChannel.play(bounce)
            gameState[0] = button.command