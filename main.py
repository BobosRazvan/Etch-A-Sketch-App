import turtle

screen = turtle.Screen()
screen.bgcolor("white")

def setup_turtle():
    global my_turtle
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)

    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(rotate_counter_clock, "a")
    screen.onkey(rotate_clock, "d")

def clear_screen():
    screen.clear()
    setup_turtle()

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def rotate_counter_clock():
    my_turtle.left(10)

def rotate_clock():
    my_turtle.right(10)

setup_turtle()
screen.onkey(clear_screen, "c")

screen.listen()
screen.exitonclick()