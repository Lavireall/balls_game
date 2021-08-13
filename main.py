import random
from tkinter import *
import time
from Ball import Ball

tk = Tk()
tk.title("Balls Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


class BallFabric:
    def create_ball(self):
        return Ball()

class BlueBallFabric(BallFabric):
    def create_ball(self, pos):
        blue_ball = Ball(canvas, pos, 'blue', -1)
        return blue_ball

class RedBallFabric(BallFabric):
    def create_ball(self, pos):
        red_ball = Ball(canvas, pos, 'red', -3)
        return red_ball

class YellowBallFabric(BallFabric):
    def create_ball(self, pos):
        yellow_ball = Ball(canvas, pos, 'yellow', 3)
        return yellow_ball


red = RedBallFabric()
blue = BlueBallFabric()
yel = YellowBallFabric()

red_balls = []
for i in range(random.randint(5, 30)):
    r = red.create_ball([random.randint(10, 490), random.randint(10, 390)])
    red_balls.append(r)
blue_balls = []
for i in range(random.randint(5, 30)):
    b = blue.create_ball([random.randint(10, 490), random.randint(10, 390)])
    blue_balls.append(b)
yel_balls = []
for i in range(random.randint(5, 30)):
    y = yel.create_ball([random.randint(10, 490), random.randint(10, 390)])
    yel_balls.append(y)


while True:
    print(len(red_balls))
    for i in red_balls:
        i.draw()
    print(len(blue_balls))
    for i in blue_balls:
        i.draw()
    # blue_ball.draw()
    print(len(yel_balls))
    for i in yel_balls:
        i.draw()
    # yel_ball.draw()

    tk.update()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.03)
