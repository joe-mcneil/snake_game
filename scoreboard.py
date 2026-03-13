from turtle import Turtle

FONT = ('Courier', 24, 'bold')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.pendown()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        with open("data.txt") as data:
            hs = data.read()
            hs = int(hs)
        self.high_score = hs
        self.keep_score()
        self.game_cont = True

    def keep_score(self):
        self.clear()
        self.teleport(x=0, y=260)
        self.write(arg=f"Score: {self.score}         High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.reset()
        self.teleport(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.teleport(0, -40)
        self.write(arg=f"PRESS ENTER TO CONTINUE", align=ALIGNMENT, font=FONT)
        self.game_cont = False

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as new_data:
            new_data.write(f"{self.high_score}")
        self.score = 0
        self.teleport(x=0, y=260)
        self.keep_score()

    def game_continue(self):
        self.game_cont = True
