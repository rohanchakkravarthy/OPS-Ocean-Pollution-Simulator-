import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Ocean Background")
screen.setup(width=1000, height=600)
screen.bgcolor("lightblue")  # Sky / water background

# Draw the ocean
ocean = turtle.Turtle()
ocean.hideturtle()
ocean.speed(0)
ocean.penup()
ocean.goto(-500, -100)
ocean.pendown()
ocean.color("deep sky blue")
ocean.begin_fill()
ocean.goto(500, -100)
ocean.goto(500, -300)
ocean.goto(-500, -300)
ocean.goto(-500, -100)
ocean.end_fill()

# Draw the sun
sun = turtle.Turtle()
sun.hideturtle()
sun.penup()
sun.goto(350, 200)
sun.color("yellow")
sun.begin_fill()
sun.circle(50)
sun.end_fill()

# Draw some waves
waves = turtle.Turtle()
waves.hideturtle()
waves.speed(0)
waves.penup()
for y in range(-120, -280, -20):
    waves.goto(-500, y)
    waves.pendown()
    waves.color("skyblue")
    waves.width(2)
    for x in range(-500, 500, 20):
        waves.goto(x, y + ((x % 40) - 20)//4)
    waves.penup()

# Draw some clouds
cloud = turtle.Turtle()
cloud.hideturtle()
cloud.penup()
cloud.goto(-300, 250)
cloud.color("white")
cloud.begin_fill()
for _ in range(2):
    cloud.circle(40,90)
    cloud.circle(40//2,90)
cloud.end_fill()

cloud.goto(-200, 230)
cloud.begin_fill()
for _ in range(2):
    cloud.circle(30,90)
    cloud.circle(30//2,90)
cloud.end_fill()

# Keep window open
turtle.done()
