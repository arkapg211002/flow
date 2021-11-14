import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen().bgcolor('black')
t.color('white')
t.speed(0)
t.width(5)
n=200
h=0
for i in range(50):
    t.right(85)
    for b in range(i-10):
        t.forward(i)
        c=colorsys.hsv_to_rgb(h,1,0.8)
        h+=1/n
        t.color(c)
turtle.exitonclick()