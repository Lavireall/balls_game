
class Ball:
    def __init__(self, canvas, place, color, velocity):
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_oval(10, 10, 30, 30, fill=self.color)
        self.canvas.move(self.id, place[0], place[1])
        self.x = velocity
        self.y = -3
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<Button-1>', self.start_game)

    def change_color(self):
        color = self.color
        if color == 'red':
            self.color = 'yellow'
            self.canvas.itemconfig(self.id, fill='yellow')
        elif color == 'yellow':
            self.color = 'red'
            self.canvas.itemconfig(self.id, fill='red')


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.change_color()
        if pos[0] <= 0:
            self.x = 3
            self.change_color()
        if pos[1] <= 0:
            self.y = 3
            self.change_color()
        if pos[3] >= self.canvas_height:
            self.y = -3
            self.change_color()


    def start_game(self, evt):
        self.started = True

# class BallFabric:
#     def __init__(self, canvas, place, color, velocity):
#         self.canvas = canvas
#         self.color = color
#         self.id = canvas.create_oval(10, 10, 30, 30, fill=self.color)
#         self.canvas.move(self.id, place[0], place[1])
#         self.x = velocity
#
#     def create_ball(self):
#         return Ball()
#
# class BlueBallFabric:
#     def create_ball(self):
#         blue_ball = Ball(canvas, [245, 130], 'blue', -1)
#         return blue_ball
#
#     class RedBallFabric:
#         def create_ball(self):
#             red_ball = Ball(canvas, [245, 100], 'red', -3)
#             return red_ball
#
#     class YellowBallFabric:
#         def create_ball(self):
#             yellow_ball = Ball(canvas, [260, 100], 'yellow', 3)
#             return yellow_ball

