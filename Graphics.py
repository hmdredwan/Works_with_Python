from turtle import * 
from colorsys import *
import turtle

turtle.title("Redwan's Graphics")
turtle.bgcolor("black")

star= turtle.Turtle()
star.speed(20)
star.pencolor("green")


for i in range(500):
    star.fd(i)
    star.lt(500)

turtle.clear()
turtle.clearscreen()


turtle.bgcolor("black")
squary= turtle.Turtle()
squary.speed(20)
squary.pencolor("red")

for j in range(400):
    squary.fd(j)
    squary.lt(91)


turtle.clear()
turtle.clearscreen()

from turtle import * 
from colorsys import *

bgcolor("black")
tracer(100)
pensize(2)
h=0

def draw(ang, n):
    circle(5+n, 69)
    left(ang)
    circle(5+2*n, 60)

goto(0,0)

for k  in range(180):
    c=hsv_to_rgb(h,1,1)
    h += 0.005
    color(c)
    up()
    draw(90, k)
    draw(180, k)
    down()
    draw(1/2, k-k)
    draw(180, k/2)
    draw(120, k-k)
    

