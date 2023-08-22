from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()
        self.starting_position = position
        self.goto(self.starting_position)

    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

