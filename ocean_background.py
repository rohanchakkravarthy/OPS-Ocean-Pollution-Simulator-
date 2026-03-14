import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Refined Ocean Ecosystem")
screen.setup(width=1000, height=600)
screen.bgcolor("lightblue")

# Ocean floor (sand)
sand_y = -200  # top of sand line
floor = turtle.Turtle()
floor.hideturtle()
floor.speed(0)
floor.penup()
floor.goto(-500, -300)
floor.pendown()
floor.color("sandybrown")
floor.begin_fill()
floor.goto(500, -300)
floor.goto(500, sand_y)
floor.goto(-500, sand_y)
floor.goto(-500, -300)
floor.end_fill()

# Draw coral
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

for i in range(-400, 401, 100):
    draw_coral(i, sand_y, random.choice(["red","orange","pink"]))

# Draw seaweed
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

for i in range(-450, 451, 50):
    draw_seaweed(i, sand_y)

# Create fish
fish_colors = ["yellow", "orange", "purple", "pink", "cyan"]
fish_list = []

for _ in range(15):
    f = turtle.Turtle()
    f.shape("triangle")  # use triangle to simulate fish
    f.penup()
    f.speed(1)
    
    # Random position above sand
    x = random.randint(-450, 450)
    y = random.randint(sand_y + 20, 250)
    f.goto(x, y)
    
    # Random size variation
    size = random.uniform(0.5, 1.2)
    f.shapesize(stretch_wid=0.5*size, stretch_len=1*size)
    
    f.color(random.choice(fish_colors))
    # Random initial heading
    f.setheading(random.randint(0, 360))
    
    fish_list.append(f)

# Move fish around
def move_fish():
    for f in fish_list:
        f.forward(random.randint(5, 15))
        f.right(random.randint(-30, 30))
        
        # Keep fish above sand and inside screen bounds
        x, y = f.position()
        if x > 500: f.goto(-500, y)
        if x < -500: f.goto(500, y)
        if y > 300: f.goto(x, 300)
        if y < sand_y + 20: f.goto(x, sand_y + 20)
        
    screen.ontimer(move_fish, 250)

move_fish()

# Keep window open
turtle.done()
