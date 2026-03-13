from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle()
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.shape("square")
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def reset(self):
        # Resets the snake to starting position and removes association with the previous snake.
        for segment in self.segments:
            segment.teleport(x=1000, y=0)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def do_nothing(self):
        pass
