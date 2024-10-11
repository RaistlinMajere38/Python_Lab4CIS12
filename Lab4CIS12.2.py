import turtle
import random

def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t, radius):
    t.circle(radius)

def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def draw_pumpkin(t, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()

    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    t.fillcolor("green")
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.forward(radius // 2)
    t.right(90)
    t.forward(radius // 5)
    t.right(90)
    t.forward(radius // 2)
    t.right(90)
    t.forward(radius // 5)
    t.end_fill()

def draw_eye(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.setheading(-60)
    for _ in range(5):
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()

def draw_star(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_sky(t, num_stars, min_y, max_y):
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(min_y, max_y)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)


screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)


t = turtle.Turtle()
t.speed(0)
t.hideturtle()


draw_pumpkin(t, -150, -150, 100)
draw_eye(t, -190, -60, 30)
draw_eye(t, -110, -60, 30)
draw_mouth(t, -150, -100, 80)

draw_pumpkin(t, 0, -150, 80)
draw_eye(t, -20, -70, 25)
draw_eye(t, 20, -70, 25)
draw_mouth(t, 0, -100, 60)

draw_pumpkin(t, 150, -150, 100)
draw_eye(t, 110, -60, 30)
draw_eye(t, 190, -60, 30)
draw_mouth(t, 150, -100, 80)


draw_sky(t, 30, 0, 300)


turtle.exitonclick()
