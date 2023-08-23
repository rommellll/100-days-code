from turtle import Turtle
FONT = ("Arial", 10, "normal")


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def update_board(self, state, x, y):
        self.goto(x, y)
        self.write(f"{state}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Congratulations! You guessed it all!", align="center", font=FONT)