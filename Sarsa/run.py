from maze import Maze
from rl import SarsaTable


def update():
    for episode in range(30):
        # initial observation
        observation = env.reset()
        # RL choose action based on observation
        action = RL.choose_action(str(observation))

        while True:
            # fresh env
            # env.render()
            print("action",action)
            # RL take action and get next observation and reward
            observation_, reward, done = env.step(observation,action)
            print("step_obs",observation_)

            # RL choose action based on step_obs
            action_ = RL.choose_action(str(observation_))
            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_),action_)

            # next observation and action (s_ and a_)
            observation = observation_
            action =  action_
            # break while loop when end of this episode
            if done:
                print("this episode is over")
                break

    # end of game
    print('game over')

if __name__ == "__main__":
    env = Maze()
    RL = SarsaTable(actions=list(range(env.n_actions)))
    update()
    print(RL.q_table)
