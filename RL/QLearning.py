import numpy as np
from MDP import *

num_states = (num_row*num_col)**2
num_episodes = 10000

def to_scalar(state):
    self_x, self_y, opp_x, opp_y = state
    return self_x * num_row**3 + self_y * num_row**2 + opp_x * num_row + opp_y

def Q_learning():
    alpha = 0.1
    gamma = 0.9

    L = np.zeros(num_episodes)
    
    num_wins = 0
    Q = np.zeros([num_states, num_actions])
    for ep in range(num_episodes):
        state = MDP_initial_state()
        epsilon = 1.0 - ep/float(num_episodes-1)
        L[ep] = float(num_wins)/(ep+1)*100
        while True:
            state_scalar = to_scalar(state)

            if np.random.random() < epsilon:
                action = np.random.randint(0,num_actions)
            else:
                action = Q[state_scalar].argmax()
                
            r, state_next, terminate = MDP_transition(state, action)
            if to_scalar(state_next) >= num_states or to_scalar(state_next) <= 0:
                break
            maxQ_next = np.max(Q[to_scalar(state_next)])
            Q[state_scalar][action] += alpha * (r + gamma * maxQ_next - Q[state_scalar][action])

            if terminate:
                if r > 0: num_wins += 1
                break
            state = state_next
                
        if ep%100 == 0:
            print ("Episode %d:" %ep, (float(num_wins)/(ep+1)*100))
    return Q, L


def run():
    Q, L  = Q_learning()

    f = open("Q_table.txt", "w")
    for i in range(num_states):
        for j in range(num_actions):
            f.write(str(Q[i][j]) + "\n")
    f.close()


    f2 = open("episode.txt", "w")
    for i in range(num_episodes):
        f2.write(str(L[i]) + "\n")
    f2.close()

run()
