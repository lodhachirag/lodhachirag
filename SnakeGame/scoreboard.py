from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()


    def Score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def Gameover(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.clear()
        self.write("Game Over", align=ALIGNMENT,font=FONT)
        self.goto(0, -60)
        self.write(f"Final Score : {self.score}" , align=ALIGNMENT,font=FONT)
