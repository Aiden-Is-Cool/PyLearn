import turtle
import os
import math
import random

#Screen

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Border

border_pen = turtle.Turtle()
border_pen.speed(10)
border_pen.hideturtle()
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(7)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

#Score to zero
score = 0

#Draw the score

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: %s" %score
score_pen.hideturtle()
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

 
#Player

player = turtle.Turtle()
player.color("yellow")
player.fillcolor("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setheading(90)
player.setposition(0, -270)

playerspeed = 15

#Create Bindings

def move_left():
    x = player.xcor()
    if x < -280:
        x = - 280
    x -= playerspeed
    player.setx(x)

def move_right():
    x = player.xcor()
    if x > 280:
        x = 280
    x += playerspeed
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs change
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#Keyboard Bindings

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "Up")

#Multiple Enemys

number_of_enemies = 5

enemies = []

for i in range(number_of_enemies):
    #CreateEnemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.fillcolor("black")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    X = random.randint(-200, 200)
    Y = random.randint(100, 250)
    enemy.setposition(X, Y)

enemyspeed = 2

#Player Bullets
bullet = turtle.Turtle()
bullet.color("black")
bullet.fillcolor("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet.setposition(-1000, -1000)

bulletspeed = 30

#Define Bullet State
#Ready to fire
#Bullet is firing
bulletstate = "ready"

#Game Loop

while True:

    for enemy in enemies:
        #Movement for enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            #Change Direction
            enemyspeed *= -1
            

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 30
                e.sety(y)
            #Change Direction
            enemyspeed *= -1

        #ColisionCheckForBullet
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

        #Bullet/EnemyColision
        if isCollision(bullet, enemy):
            #BulletReset
            bullet.hideturtle()
            bullletstate = "ready"
            bullet.setposition(0, -400)
            #ResetEnemy
            enemy.setposition(X, Y)
            
            #Score Update
            
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

            if isCollision (enemy, player):
                bullet.hideturtle()
                player.hideturtle()
                enemy.hideturtle()
                break

    #MoveBullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #ColisionCheckForBullet
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    #Bullet/EnemyColision
    if isCollision(bullet, enemy):
        #BulletReset
        bullet.hideturtle()
        bullletstate = "ready"
        bullet.setposition(0, -400)
        #ResetEnemy
        enemy.setposition(-200, 250)

    if isCollision (enemy, player):
        bullet.hideturtle()
        player.hideturtle()
        enemy.hideturtle()
        break


    

turtle.Screen().exitonclick()