from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.new_point()


    def new_point(self):
        self.clear()
        self.color("black")
        self.goto(-230, 250)
        self.write(f"LEVEL {self.score}", align="left", font=FONT)
        self.score += 1

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 40, "bold"))
