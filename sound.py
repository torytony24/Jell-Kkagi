import pygame

pygame.mixer.init()

mainChannel = pygame.mixer.Channel(0)
mainChannel.set_volume(0.3)
mainBGM = pygame.mixer.Sound("resources/soundtracks/mainBGM.mp3")
mainChannel.play(mainBGM)

subChannel = pygame.mixer.Channel(1)
subChannel.set_volume(0.8)
gameEnd = pygame.mixer.Sound("resources/soundtracks/gameEnd.mp3")

effectChannel = pygame.mixer.Channel(2)
effectChannel.set_volume(0.5)
bounce = pygame.mixer.Sound("resources/soundtracks/bounce.mp3")

signal = True
def subChannel_signal():
    global signal
    if signal:
        subChannel.play(gameEnd)
        signal = False