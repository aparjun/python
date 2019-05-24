from turtle import *

wn = Screen()
wn.setup(500,500)
turtle = Turtle()
turtle.speed("fastest")

step = 100
def draw_square(length,angle):
    if(angle<=93):
        turtle.forward(length)
        turtle.right(angle)
        return draw_square(length,angle+1)
    elif(length<=200):
        angle=90
        return draw_square(length+1,angle)
    else:
        return

draw_square(100,90)
                                            
