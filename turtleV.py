import turtle
import random

# Define the speed of the game
game_speed = 1000

# Screen setup
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(game_speed)  # Set the animation speed using the game_speed variable


# Snake setup
snake = []
snake_length = 3

# Create the initial snake segments
for i in range(snake_length):
    segment = turtle.Turtle()
    segment.speed(0)
    segment.shape("square")
    segment.color("white")
    segment.penup()
    segment.goto(-20 * i, 0)
    snake.append(segment)

# Food setup
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake movement
def move():
    # Determine the new head position based on the current heading
    heading = snake[0].heading()
    x = snake[0].xcor()
    y = snake[0].ycor()

    if heading == 0:   x += 20  # Right
    elif heading == 180: x -= 20 # Left
    elif heading == 90:  y += 20 # Up
    elif heading == 270: y -= 20 # Down

    # Move the tail segments to follow the head
    for i in range(len(snake) - 1, 0, -1):
        x_prev = snake[i - 1].xcor()
        y_prev = snake[i - 1].ycor()
        snake[i].goto(x_prev, y_prev)

    # Move the head to the new position
    if len(snake) > 0:
        snake[0].goto(x, y)


# Keyboard controls
def go_left():
    if snake[0].heading() != 0:
        snake[0].setheading(180)

def go_right():
    if snake[0].heading() != 180:
        snake[0].setheading(0)

def go_up():
    if snake[0].heading() != 270:
        snake[0].setheading(90)

def go_down():
    if snake[0].heading() != 90:
        snake[0].setheading(270)

window.listen()
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")


try:
    # Main loop
    while True:
        window.update()
        move()

        # Check collision with food
        if snake[0].distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            # Add a new segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            snake.append(new_segment)

        # Move the end segments first
        for i in range(len(snake) - 1, 0, -1):
            x = snake[i - 1].xcor()
            y = snake[i - 1].ycor()
            snake[i].goto(x, y)
        if len(snake) > 0:
            x = snake[0].xcor()
            y = snake[0].ycor()
            snake[-1].goto(x, y)

        # Collision with the border
        if snake[0].xcor() > 290 or snake[0].xcor() < -290 or snake[0].ycor() > 290 or snake[0].ycor() < -290:
            window.bye()
            break

        # Collision with self
        for segment in snake[1:]:
            if segment.distance(snake[0]) < 10:
                window.bye()
                break
except turtle.Terminator:
    pass
