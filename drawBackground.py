from settings import *

def drawBackground(screen, time, bgImages, gameState):
    ground = bgImages[-1]
    bgWidth = ground.get_width()
    bgHeight = ground.get_height()
    for x in range(1000):
        speed = 1
        if gameState[0] == 'startMenu':
            for bgImage in bgImages[:-1]:
                screen.blit(bgImage, ((x * bgWidth) - time * speed, 0))
                speed += 0.2
            speed += 0.2
            screen.blit(ground, ((x * bgWidth) - time * 2.5, HEIGHT - bgHeight))
        else:
            for bgImage in bgImages[:4]+bgImages[5:-1]:
                screen.blit(bgImage, ((x * bgWidth) - time * speed, 0))
                speed += 0.2





