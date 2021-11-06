from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1


    def movement(self):
        x_cor = self.xcor() + self.x_move         # every time the screen updates the ball moves 10 units on X axis
        y_cor = self.ycor() + self.y_move           # every time the screen updates the ball moves 10 units on X axis
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1       # inorder to change direction we need to make y axis value to -10
                                # so self.y_move *= -1 == -10       (the movement is like a invertes V)

    def bounce_x(self):
        self.x_move *= -1        # inorder to change direction we need to make x axis value to -10
        self.ball_speed *= 0.9                        # so self.x_move *= -1 == -10       (the movement is like this > )

    def ball_reset(self):
        self.goto((0, 0))
        self.ball_speed = 0.1
        self.bounce_x()