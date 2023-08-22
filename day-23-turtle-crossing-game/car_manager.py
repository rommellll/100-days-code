from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.generate_car()
        self.car_speed = 0.1

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_len=2)
            y = random.randint(-250, 280)
            car.goto(250, y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_car_speed(self):
        self.car_speed *= 0.9
