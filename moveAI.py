import random
from settings import *
import numpy as np

num_row = 10
num_col = 10
num_actions = 5

num_states = (num_row*num_col)**2

def get_action(state):        
    Q = np.zeros([num_states, num_actions])
    f = open("resources/Q_table/Q_table.txt", "r")
    for i in range(num_states):
        for j in range(num_actions):
            Q[i][j] = float(f.readline().strip())
    state_scalar = to_scalar(state)
    action = Q[state_scalar].argmax()
    return action

def to_scalar(state):
    self_x, self_y, opp_x, opp_y = state
    return self_x * num_row**3 + self_y * num_row**2 + opp_x * num_row + opp_y


def moveAI(screen, stones, gameState):
    player1Stones = []
    player2Stones = []
    for stone in stones:
        if stone.player == 'player1':
            player1Stones.append(stone)
        else:
            player2Stones.append(stone)
    if len(player1Stones) == 0 or len(player2Stones) == 0:
        pass
    else:
        player1Stone = random.choice(player1Stones)
        player2Stone = random.choice(player2Stones)
        
        self_x, self_y = int(player2Stone.x + LENGTH//2)//10, int(player2Stone.y + LENGTH//2)//10
        opp_x, opp_y = int(player1Stone.x + LENGTH//2)//10, int(player1Stone.y + LENGTH//2)//10

        state = [self_x, self_y, opp_x, opp_y]
        action = get_action(state)

        for particle in player2Stone.particleList:
            particle.vx = (opp_x - self_x) * (action+10)
            particle.vy = (opp_y - self_y) * (action+10)

