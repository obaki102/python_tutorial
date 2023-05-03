from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score_text()
        self.hideturtle()
        
    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_score_text()
        
    def update_score_text(self):
         self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
         
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)