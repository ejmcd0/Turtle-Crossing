from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10





class CarManager():
    def __init__(self):
        self.traffic = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_new_car(self):
        chance = random.randint(1, 6)
        if chance == 3:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            self.traffic.append(new_car)

    def driving(self):
        for car in self.traffic:
            car.backward(self.car_speed)

    def go_faster(self):
        self.car_speed += MOVE_INCREMENT


