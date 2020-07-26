#daddygame, part 1
#screen setup
#python 3.8

import turtle
import os

#set up the screen
mainWn = turtle.Screen()
mainWn.bgcolor("black")
mainWn.title("Daddy Game")

#Draw a border


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(10)
border_pen.pendown()
for sides in range(4):
    border_pen.fd(600)
    border_pen.left(90)
    
border_pen.hideturtle()


player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("triangle")
player.fillcolor("green")
player.setheading(90)
player.pencolor("yellow")
player.setpos(0,-250)

playerspeed=15
def moveleft():
    x = player.xcor()
    x-= playerspeed
    player.setx(x)

def moveright():
    x = player.xcor()
    x+= playerspeed
    player.setx(x)

#Create Keyboardbindings
turtle.listen()
turtle.onkey(moveleft,"Left")
turtle.onkey(moveright,"Right")

turtle.Screen().exitonclick()

