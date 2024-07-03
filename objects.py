import pygame
import numpy as np
from math import *
from scipy import interpolate
from settings import *
from conv3D import *
from sound import *

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



class ButtonJelly:
    def __init__(self, x, y, width, height, command):
        self.x = x
        self.y = y
        self.k = 2000
        self.width = width
        self.height = height
        self.command = command
        self.hitbox = 20
        upperSide = [Particle(x - width//2 + i*width/10, y + height//2, self.k, self.hitbox) for i in range(1,10)]
        rightSide = [Particle(x + width//2, y + height//2 - i*height//5, self.k, self.hitbox) for i in range(1,5)]
        lowerSide = [Particle(x + width//2 - i*width//10, y - height//2, self.k, self.hitbox) for i in range(1,10)]
        leftSide = [Particle(x - width//2, y - height//2 + i*height//5, self.k, self.hitbox) for i in range(1,5)]
        self.particleList = upperSide + rightSide + lowerSide + leftSide
        n = len(self.particleList)
        for i in range(n):
            for j in range(n):
                if i != j:
                    self.particleList[i].connected.add((self.particleList[j],self.particleList[i].dist(self.particleList[j])))
        centerParticle = Particle(x, y, self.k, self.hitbox)
        centerRightParticle = Particle(x + width//2, y + width//2, self.k, self.hitbox)
        centerLeftParticle = Particle(x - width//2, y + width//2, self.k, self.hitbox)
        centerUpperParticle = Particle(x + width//2, y - width//2, self.k, self.hitbox)
        centerLowerParticle = Particle(x - width//2, y - width//2, self.k, self.hitbox)
        for particle in self.particleList:
            particle.connected.add((centerParticle, particle.dist(centerParticle)))
            particle.connected.add((centerRightParticle, particle.dist(centerRightParticle)))
            particle.connected.add((centerLeftParticle, particle.dist(centerLeftParticle)))
            particle.connected.add((centerUpperParticle, particle.dist(centerUpperParticle)))
            particle.connected.add((centerLowerParticle, particle.dist(centerLowerParticle)))

    def draw(self, screen):
        x = np.array([particle.x for particle in self.particleList])
        y = np.array([particle.y for particle in self.particleList])
        x = np.r_[x, x[0]]
        y = np.r_[y, y[0]]
        tck, _ = interpolate.splprep([x, y], s=0, per=True)
        xi, yi = interpolate.splev(np.linspace(0, 1, 1000), tck)
        for i in range(len(xi)):
            if i%5==0:
                pygame.draw.circle(screen,subTheme,(xi[i] + 5, yi[i] + 5),5)
        for i in range(len(xi)):
            if i%5==0:
                pygame.draw.circle(screen,mainTheme,(xi[i], yi[i]),5)

    def update(self, mouse):
        for particle in self.particleList:
            particle.update()
        self.collideUpdate(mouse)

    def collideUpdate(self, mouse):
        mouseX, mouseY = mouse.get_pos()
        for particle in self.particleList:
            if calcDist(particle.x, particle.y, mouseX, mouseY) <= particle.hitbox:
                particle.vx += 5 * (particle.x - mouseX)
                particle.vy += 5 * (particle.y - mouseY)

crown = [(-0.7,0.5), (-1,1), (-0.7,0.9), (-0.6,1.2), (-0.4,1), (-0.3,1.3), (-0.1,0.7)]

class Stone:
    def __init__(self, x, y, r, player, isKing):
        self.x = x
        self.y = y
        self.r = r
        self.k = 5000
        self.hitbox = 120
        self.particleList = [Particle(self.x+self.r*cos(2*pi/n*i), self.y+self.r*sin(2*pi/n*i), self.k, self.hitbox) for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    self.particleList[i].connected.add((self.particleList[j],self.particleList[i].dist(self.particleList[j])))
        self.player = player
        self.isKing = isKing

    def draw(self, screen):
        x = np.array([particle.x for particle in self.particleList])
        y = np.array([particle.y for particle in self.particleList])
        x = np.r_[x, x[0]]
        y = np.r_[y, y[0]]
        tck, _ = interpolate.splprep([x, y], s=0, per=True)
        xi, yi = interpolate.splev(np.linspace(0, 1, 1000), tck)
        borderPoints = [conv3D(xi[i],yi[i]) for i in range(0,len(xi),15)]
        nPoints = len(borderPoints)

        if self.player == 'player1':   # (242,55,233)
            for i in range(nPoints):
                pygame.draw.line(screen, (243,90,204), borderPoints[i], borderPoints[(i+nPoints//2)%nPoints], 7)
            for i in range(nPoints):
                pygame.draw.circle(screen,(242,125,175),borderPoints[i],5)
            pygame.draw.line(screen, (180, 40, 174), conv3D(self.x+self.r*0.25, self.y+self.r*0.25), conv3D(self.x+self.r*0.01, self.y+self.r*0.25), 4)
            pygame.draw.line(screen, (180, 40, 174), conv3D(self.x+self.r*0.25, self.y-self.r*0.25), conv3D(self.x+self.r*0.01, self.y-self.r*0.25), 4)
            if self.isKing:
                pygame.draw.polygon(screen, (255,223,0), [conv3D(self.x - self.r * posX, self.y - self.r * posY) for posX, posY in crown])

        else:                          # (180,54,242)
            for i in range(nPoints):
                pygame.draw.line(screen, (205,105,197), borderPoints[i], borderPoints[(i+nPoints//2)%nPoints], 7)
            for i in range(nPoints):
                pygame.draw.circle(screen,(221,139,167),borderPoints[i],5)
            pygame.draw.line(screen, (133,39,180), conv3D(self.x-self.r*0.25, self.y+self.r*0.25), conv3D(self.x-self.r*0.01, self.y+self.r*0.25), 4)
            pygame.draw.line(screen, (133,39,180), conv3D(self.x-self.r*0.25, self.y-self.r*0.25), conv3D(self.x-self.r*0.01, self.y-self.r*0.25), 4)
            if self.isKing:
                pygame.draw.polygon(screen, (255,223,0), [conv3D(self.x + self.r * posX, self.y + self.r * posY) for posX, posY in crown])

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

    def outOfBoard(self):
        if self.x > LENGTH//2:
            return True
        elif self.x < -LENGTH//2:
            return True
        elif self.y > LENGTH//2:
            return True
        elif self.y < -LENGTH//2:
            return True
        else:
            return False