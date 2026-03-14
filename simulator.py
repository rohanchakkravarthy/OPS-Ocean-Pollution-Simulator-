import turtle
import random

screen = turtle.Screen()
screen.bgcolor("blue")
screen.setup(width=900, height=600)

# Fish
fish = turtle.Turtle()
fish.shape("circle")
fish.color("yellow")
fish.penup()
fish.speed(0)
fish.goto(random.randint(-400,400), random.randint(-250,250))

# Pollution
pollution = turtle.Turtle()
pollution.shape("circle")
pollution.color("brown")
pollution.penup()
pollution.speed(0)
pollution.goto(random.randint(-400,400), random.randint(-250,250))

turtle.done()
