import numpy as np
from math import *
import pygame

num_row = 10
num_col = 10
num_actions = 5


def MDP_transition(state, action):
    
    state_next = move(state, action)
    self_x, self_y, opp_x, opp_y = state_next
    
    if not out_of_board(self_x, self_y): 
        if out_of_board(opp_x, opp_y):
            reward = 1
        else:
            reward = 0
    else:
        reward = -1
    terminate = True

    return reward, state_next, terminate

def MDP_initial_state():  # randomly generate initial state
    self_x = np.random.randint(num_row)
    self_y = np.random.randint(num_col)
    opp_x = np.random.randint(num_row)
    opp_y = np.random.randint(num_col)

    return [self_x, self_y, opp_x, opp_y]
    

def move(state, action):
    self_x, self_y, opp_x, opp_y = state

    self_stone = Stone(self_x * 10, self_y * 10)
    opp_stone = Stone(opp_x * 10, opp_y * 10)

    stones = [self_stone, opp_stone]

    for i in range(num_actions):
        if action == i:
            for particle in self_stone.particleList:
                particle.vx = (opp_x - self_x) * (i+10)
                particle.vy = (opp_y - self_y) * (i+10)

    particle = self_stone.particleList[0]
    while particle.vx**2 + particle.vy**2 >= 0.1:
        self_stone.update(stones)
        opp_stone.update(stones)


    self_x = int(self_stone.x)//10
    self_y = int(self_stone.y)//10
    opp_x = int(opp_stone.x)//10
    opp_y = int(opp_stone.y)//10

    return [self_x, self_y, opp_x, opp_y]


def out_of_board(x,y):
    if x >= 100:
        return True
    elif x <= 0:
        return True
    elif y >= 100:
        return True
    elif y <= 0:
        return True
    else:
        return False


dt = 0.01
m = 100
d = 100
n = 15
e = 1.01

def calcDist(x1, y1, x2, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

def centM(L):
    n = len(L)
    return (sum([L[i].x for i in range(n)])/n, sum([L[i].y for i in range(n)])/n)

class Particle:
    def __init__(self, x, y, k, hitbox):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.k = k
        self.hitbox = hitbox
        self.Fx = 0
        self.Fy = 0
        self.connected = set()

    def dist(self,P):
        return calcDist(self.x, self.y, P.x, P.y)

    def update(self):
        for P, L in self.connected:
            r = self.dist(P)
            F = self.k*(r-L)
            self.Fx = F*(P.x-self.x)/r + d*(P.vx-self.vx)
            self.Fy = F*(P.y-self.y)/r + d*(P.vy-self.vy)
            self.vx += self.Fx*dt/m
            self.vy += self.Fy*dt/m
            self.x += self.vx*dt
            self.y += self.vy*dt
        if abs(self.vx) > 0:
            self.vx *= 0.85
        if abs(self.vy) > 0:
            self.vy *= 0.85

    def collided(self, particle):
        return calcDist(self.x, self.y, particle.x, particle.y) <= self.hitbox + particle.hitbox

class Stone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 5
        self.k = 5000
        self.hitbox = 120
        self.particleList = [Particle(self.x+self.r*cos(2*pi/n*i), self.y+self.r*sin(2*pi/n*i), self.k, self.hitbox) for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    self.particleList[i].connected.add((self.particleList[j],self.particleList[i].dist(self.particleList[j])))

    def draw(self, screen):
        for particle in self.particleList:
            pygame.draw.circle(screen,'white',(particle.x, particle.y),5)

    def update(self, stones):
        for particle in self.particleList:
            particle.update()
        self.x, self.y = centM(self.particleList)
        for stone in stones:
            if calcDist(self.x, self.y, stone.x, stone.y) <= self.r + stone.r and self != stone:
                self.collideUpdate(stone)
        
    def collideUpdate(self, stone):
        for particleA in self.particleList:
            for particleB in stone.particleList:
                if particleA.collided(particleB):
                    tmpX, tmpY = particleB.vx, particleB.vy
                    particleB.vx, particleB.vy = e * particleA.vx, e * particleA.vy
                    particleA.vx , particleA.vy = e * tmpX, e * tmpY
    
    def move(self, mousePos):
        cenX, cenY = conv3D(self.x, self.y)
        for particle in self.particleList:
            vy = (cenX - mousePos[0]) * 0.2
            vx = (cenY - mousePos[1]) * 0.2
            theta_ = theta[0]
            particle.vx = vx * cos(theta_) - vy * sin(theta_)
            particle.vy = vx * sin(theta_) + vy * cos(theta_)



