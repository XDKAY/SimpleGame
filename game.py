import turtle
import random

from config import Config
from player import Player
from food import Food
from game_map import GameMap


class Text:
    def __init__(self, text, position:tuple):
        self.text = text
        self.x, self.y = position
    
    def write(self):
        turtle.clear()
        turtle.hideturtle()
        turtle.penup()
        turtle.setposition(self.x, self.y)
        turtle.write(self.text, align='center', font=('Arial', 24, 'normal'))
    
    def update(self, new_text):
        self.text = new_text


class Game:
    def __init__(self):
        self.config = Config()

        self.__screen = turtle.Screen()
        self.__screen.bgcolor(self.config.SCREEN_BG)
        self.__screen.screensize(self.config.SCREEN_SIZE, self.config.SCREEN_SIZE)

        self.__game_map = GameMap()
        self.__game_map.draw_game_map()
        self.player = Player()

        self.text_amount_food = Text(
            text=f'Amount food\t{self.player.describe_amount_food()}', 
            position=(0, self.config.SCREEN_SIZE)
        )
        self.text_amount_food.write()

        self.text_game_over = Text(
            text='Game Over',
            position=(0, 0)
        )

        self.__foods = []

    def __draw_food(self):
        while len(self.__foods) < 20:
            food = Food(
                x=self.__random_coordinate(),
                y=self.__random_coordinate()
            )
            self.__foods.append(food)
            food.position()

    def __random_coordinate(self):
        return random.randint(-self.config.SCREEN_SIZE+10, self.config.SCREEN_SIZE-10)

    def __is_collision(self, food:Food):
        return abs(int(food.xcor() - self.player.xcor())) <= 15 and \
            abs(int(food.ycor() - self.player.ycor())) <= 15

    def eat_food(self):
        for index_food, food in enumerate(self.__foods):
            if self.__is_collision(food):
                self.__foods.remove(food)
                self.__screen.turtles().remove(food)
                self.player.update_amount_food()
                
                food.hideturtle()
                
                self.text_amount_food.text = f'Amount food\t{self.player.describe_amount_food()}'
                self.text_amount_food.write()

    def __is_wall(self):
        if any((abs(self.player.xcor()) >= self.config.SCREEN_SIZE,
            abs(self.player.ycor()) >= self.config.SCREEN_SIZE)
            ):
            return True

    def game_over(self):
        self.text_game_over.write()

    def run_game(self):
        run = True
        while run:
            self.__draw_food()
            self.__screen.listen()
            self.__screen.update()


            self.player.forward(self.player.speed())
            
            if self.__is_wall():
                self.game_over()
                run = False

            turtle.onkey(self.player.move_up, 'Up')
            turtle.onkey(self.player.move_down, 'Down')
            turtle.onkey(self.player.move_left, 'Left')
            turtle.onkey(self.player.move_right, 'Right')

            self.eat_food()
        
        self.__screen.mainloop()


if __name__ == '__main__':
    game = Game()
    game.run_game()
