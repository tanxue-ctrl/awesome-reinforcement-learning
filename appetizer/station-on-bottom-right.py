import numpy as np
import pandas as pd
import time

np.random.seed(2)  # reproducible


N_STATES = 6   # the length of the 1 dimensional world
ACTIONS = ['left', 'right']     # available actions
EPSILON = 0.9    # greedy police
ALPHA = 0.1      # learning rate
GAMMA = 0.9      # discount factor
MAX_EPISODES = 20   # maximum episodes
FRESH_TIME = 0.3    # fresh time for one move

def init_q_table(n_states,actions):
    q_tabel = pd.DataFrame(np.zeros((n_states,len(actions))),columns=actions)
    return q_tabel

def select_action(state,q_tabel):
    s_a = q_tabel.iloc[state,:]
    if (np.random.uniform()>EPSILON) or ((s_a == 0).all()):
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = s_a.idxmax()

    return action_name

def cal_reward(state,action):
    if action == "right":
        if state == N_STATES-2:     # ----#-  move right => reach terminal
            reward = 1
            next_state = "bingo"
        else:
            reward = 0               # --#--- just move right => can't reach terminal
            next_state = state + 1
    else:
        reward = 0
        if state == 0:
            next_state = state          #  #-----  reach the wall
        else:
            next_state = state - 1      #     ---#--  move left => --#---

    return reward,next_state

def update_env(state,counter,episode):
    env_list = ["-"]*N_STATES                    # env: ------
    if state == "bingo":
        interaction = 'Episode %s: total_steps = %s' % (episode+1, counter+1)
        print('\r{}'.format(interaction))
        time.sleep(0.5)
    else:
        env_list[state] = "#"
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)



def rl():
    q_table = init_q_table(N_STATES,ACTIONS)
    for episode in range(MAX_EPISODES):
        counter = 0
        state = 0
        bingo = False
        while not bingo:
            action = select_action(state,q_table)               # select action based on current state and q-table
            reward, next_state = cal_reward(state,action)       # take action, get next_state and reward
            q_predict = q_table.loc[state,action]
            if next_state != "bingo":
                q_target = reward + GAMMA*q_table.iloc[next_state,:].max()
            else:
                q_target = reward                               # this episode is over
                bingo = True

            q_table.loc[state,action] += ALPHA*(q_target - q_predict)      # update q-table
            state = next_state                                    # move to next step
            update_env(state,counter,episode)                     # visualize env
            counter += 1

    return q_table


if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)