from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.segments.append(snake_body)

    def update_snake_body(self):
        last_segment_index = len(self.segments) - 1
        last_x = self.segments[last_segment_index].xcor()
        last_y = self.segments[last_segment_index].ycor()
        new_segment = (last_x, last_y)
        self.add_segment(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        direction = self.head.heading()
        if direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        direction = self.head.heading()
        if direction != UP:
            self.head.setheading(DOWN)

    def left(self):
        direction = self.head.heading()
        if direction != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        direction = self.head.heading()
        if direction != LEFT:
            self.head.setheading(RIGHT)

