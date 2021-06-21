from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_board()

    def update_board(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def get_score(self):
        self.reset()
        self.score += 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_board()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)
