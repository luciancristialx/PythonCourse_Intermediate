from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
COLOR = "white"
class Scoreboard(Turtle):
    @staticmethod
    def get_high_score():
        with open("data.txt") as txt_file:
            high_score = txt_file.read()
            return high_score

    @staticmethod
    def write_high_score(score):
        with open("data.txt", mode = "w") as txt_file:
            txt_file.write(score)

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(Scoreboard.get_high_score())
        self.color(COLOR)
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            Scoreboard.write_high_score(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

