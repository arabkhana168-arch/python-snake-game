from turtle import Turtle
ALINGHMENT = "center"
FRONT = ("Arial", 22, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def colide(self):
        self.goto(0, 0)
        self.write(arg="Game over", align=ALINGHMENT, font=FRONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALINGHMENT, font=FRONT)


    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
