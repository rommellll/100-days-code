import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager(

)

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_is_on = True
while game_is_on:
    print(car.car_speed)
    time.sleep(car.car_speed)
    screen.update()
    car.move()
    car.generate_car()

    for car_instance in car.all_cars:
        if car_instance.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.reset()
        scoreboard.increase_level()
        car.increase_car_speed()


screen.exitonclick()

