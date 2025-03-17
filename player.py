import turtle


class Player(turtle.Turtle):
    def __init__(self, shape='turtle'):
        super().__init__(shape)

        self.__width, self.__len = (2, 2)
        self.shapesize(self.__width, self.__len)
        self.color('green')
        self.speed(4)
        self.penup()

        self.__amount_food = 0

    def move_left(self):
        self.setheading(180)

    def move_right(self):
        self.setheading(0)

    def move_up(self):
        self.setheading(90)

    def move_down(self):
        self.setheading(270)

    def update_amount_food(self):
        self.__amount_food += 1

    def describe_amount_food(self):
        return self.__amount_food


    
