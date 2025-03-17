import turtle
from config import Config


class GameMap(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='classic')
        self.config = Config()

        self.penup()
        self.pensize(5)
        self.speed(0)
        self.setposition(-self.config.SCREEN_SIZE, -self.config.SCREEN_SIZE)

    def draw_game_map(self):
        self.pendown()
        for _ in range(4):
            self.forward(2*self.config.SCREEN_SIZE)
            self.left(90)
        self.hideturtle()
