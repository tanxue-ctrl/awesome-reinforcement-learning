import time

class Maze():
    def __init__(self):
        self.action_space = ['u', 'd', 'r', 'l']
        self.n_actions = len(self.action_space)
        self.maze = [
                ["-","-","x","-"],
                ["-","-","-","-"],
                ["-","x","o","-"],
                ["-","-","-","-"]
                  ]
        self.h = len(self.maze)
        self.w = len(self.maze[0])

    def reset(self):
        ini_state = [0,0]
        return ini_state

    def step(self,s,a):
        x = s[0]
        y = s[1]
        if a == 0: # up
            if x > 0:
                s_ = [x-1,y]
            else:
                s_ = s
        elif a == 1:   # down
            if x < self.h - 1:
                s_ = [x+1,y]
            else:
                s_ = s
        elif a == 2:  # right
            if y < self.w - 1:
                s_ =[x,y+1]
            else:
                s_ = s
        else:
            if y > 0:
                s_ = [x,y-1]
            else:
                s_ = s
        if self.maze[s_[0]][s_[1]] == "o":
            reward = 1
            done = True
        elif self.maze[s_[0]][s_[1]] == "x":
            reward = -1
            done = True
        else:
            reward = 0
            done = False
        return s_, reward, done



    def render(self,s):
        time.sleep(0.1)

        # self.maze[s[0]][s[1]] = "$"
        # print(maze)



if __name__ == '__main__':
    env = Maze()

    env.render([1,1])

    env.render([1,2])