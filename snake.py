from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in starting_positions:
            self.add_segment(i)


    def add_segment(self,i):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(i)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.segments[0].forward(MOVE_FORWARD)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
