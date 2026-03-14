import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Ocean Ecosystem")
screen.setup(width=1000, height=600)
screen.bgcolor("lightblue")

# Draw ocean floor
floor = turtle.Turtle()
floor.hideturtle()
floor.speed(0)
floor.penup()
floor.goto(-500, -300)
floor.pendown()
floor.color("sandybrown")
floor.begin_fill()
floor.goto(500, -300)
floor.goto(500, -200)
floor.goto(-500, -200)
floor.goto(-500, -300)
floor.end_fill()

# Draw coral function
def draw_coral(x, y, color="red"):
    coral = turtle.Turtle()
    coral.hideturtle()
    coral.speed(0)
    coral.penup()
    coral.goto(x, y)
    coral.pendown()
    coral.color(color)
    coral.width(3)
    for _ in range(5):
        coral.goto(x + random.randint(-10, 10), y + random.randint(20, 50))
        coral.goto(x, y)

# Add multiple corals
for i in range(-400, 401, 100):
    draw_coral(i, -200, random.choice(["red","orange","pink"]))

# Draw seaweed function
def draw_seaweed(x, y, color="green"):
    weed = turtle.Turtle()
    weed.hideturtle()
    weed.speed(0)
    weed.penup()
    weed.goto(x, y)
    weed.pendown()
    weed.color(color)
    for _ in range(3):
        weed.goto(x + random.randint(-5,5), y + random.randint(30,60))
        weed.goto(x, y)

# Add seaweed
for i in range(-450, 451, 50):
    draw_seaweed(i, -200)

# Draw some fish
fish_colors = ["yellow", "orange", "purple", "pink"]
fish_list = []

for _ in range(15):
    f = turtle.Turtle()
    f.shape("turtle")
    f.color(random.choice(fish_colors))
    f.penup()
    f.speed(1)
    f.goto(random.randint(-450,450), random.randint(-100,200))
    fish_list.append(f)

# Make fish swim randomly
def move_fish():
    for f in fish_list:
        f.forward(random.randint(5, 15))
        f.right(random.randint(-30,30))
        x, y = f.position()
        if x > 500: f.goto(-500, y)
        if x < -500: f.goto(500, y)
        if y > 300: f.goto(x, -300)
        if y < -300: f.goto(x, 300)
    screen.ontimer(move_fish, 250)

move_fish()

# Keep window open
turtle.done()
