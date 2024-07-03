import pygame

# Screen size
WIDTH, HEIGHT = 1200, 900
LENGTH = 100

# Color themes
mainTheme = (250,150,150)
subTheme = (250,200,200)

# 3D constants
# Board
h = [150]
r = [100]
theta = [0.05]
rightMousePressed = [False]
leftMousePressed = [False]
originPos = [(0,0)]

# Player info
playerTurn = ['player1']
targetStone = [None]
draggedPos = [(0,0)]
movingStone = [None]
isMoving = [False]
turn180 = [0]
