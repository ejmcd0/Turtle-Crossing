import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.make_new_car()

    cars.driving()

    if player.at_finish_line():
        player.back_to_start()
        cars.go_faster()
        scoreboard.new_point()

    for car in cars.traffic:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
