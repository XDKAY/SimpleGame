import turtle


class Food(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__(shape='circle')
        self.penup()
        self.shapesize(1, 1)
        self.speed(0)
        self.color('red')
        self.x = x
        self.y = y

    def position(self):
        self.setposition(self.x, self.y)