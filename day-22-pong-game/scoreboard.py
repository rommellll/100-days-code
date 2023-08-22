from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 50, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(-200, 250)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.setposition(200, 250)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over!", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()