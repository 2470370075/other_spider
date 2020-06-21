import turtle
import time
import random

turtle.speed(10)
turtle.pensize(2)

turtle.bgcolor('#3333CC')


turtle.begin_fill()                           #地面
turtle.fillcolor('#669966')

turtle.fd(500)
for i in range(4):
    turtle.right(90)
    turtle.fd(1000)
turtle.end_fill()

turtle.speed(3)

turtle.fillcolor('black')
turtle.begin_fill()
turtle.penup()               #马路
turtle.setpos(-80,0)
turtle.pendown()
turtle.right(110)
turtle.fd(500)
turtle.left(110)
turtle.fd(500)
turtle.left(110)
turtle.fd(500)
turtle.setheading(180)
turtle.fd(100)
turtle.end_fill()

turtle.penup()
turtle.color('yellow')     #斑马线
turtle.setpos(0,-10)
turtle.pendown()

turtle.setheading(270)
for i in range(5):
    turtle.pensize(10*i)
    turtle.fd(20*i)
    turtle.penup()
    turtle.fd(40*i)
    turtle.pendown()


turtle.pensize(2)                         #   山
turtle.penup()
turtle.home()
turtle.setheading(0)
turtle.fd(200)
turtle.pendown()

turtle.fillcolor('#2C2C90')

turtle.begin_fill()
turtle.setheading(45)
turtle.fd(100)
turtle.setheading(315)
turtle.fd(50)
turtle.setheading(45)
turtle.fd(100)
turtle.setheading(315)
turtle.fd(150)
turtle.end_fill()









turtle.speed(10)
turtle.penup()
turtle.setpos(-200,-20)
for i in range(3):
    turtle.penup()
    turtle.pensize(1)
    turtle.setheading(0)

    turtle.fillcolor('green')          #树
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(70)
    turtle.circle(10,270)
    for i in range(5):
        turtle.left(140)
        turtle.circle(10,270)
    turtle.end_fill()

    turtle.fillcolor('#CC7033')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.fd(5)

    turtle.setheading(265)
    turtle.fd(40)
    turtle.setheading(0)
    turtle.fd(20)
    turtle.setheading(95)
    turtle.fd(40)
    turtle.end_fill()

    turtle.setheading(250)
    turtle.penup()
    turtle.fd(150)

turtle.penup()
turtle.setpos(200,-20)
for i in range(3):
    turtle.penup()
    turtle.pensize(1)
    turtle.setheading(0)

    turtle.fillcolor('green')          #树
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(70)
    turtle.circle(10,270)
    for i in range(5):
        turtle.left(140)
        turtle.circle(10,270)
    turtle.end_fill()

    turtle.fillcolor('#CC7033')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.fd(5)

    turtle.setheading(265)
    turtle.fd(40)
    turtle.setheading(0)
    turtle.fd(20)
    turtle.setheading(95)
    turtle.fd(40)
    turtle.end_fill()

    turtle.setheading(290)
    turtle.penup()
    turtle.fd(150)















turtle.speed(4)
turtle.pensize(2)
turtle.pencolor('yellow')                          #星星
for i in range(5):
    x = random.randint(-400,400)
    y = random.randint(50,400)
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()


    turtle.begin_fill()
    turtle.fillcolor('yellow')
    for i in range(4):
        turtle.right(-160)
        turtle.fd(30)
        turtle.right(-160)
        turtle.fd(30)
    turtle.end_fill()



turtle.penup()              #月亮
turtle.setpos(100,300)

turtle.pendown()
turtle.fillcolor('#FFFFCC')
turtle.begin_fill()
turtle.setheading(320)
turtle.circle(40,270)
turtle.setheading(340)
turtle.circle(-30,160)
turtle.end_fill()










time.sleep(40)