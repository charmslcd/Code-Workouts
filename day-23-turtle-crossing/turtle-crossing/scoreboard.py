from turtle import Turtle
FONT = ("Courier", 15, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230, 250)
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_completed(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
