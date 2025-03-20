import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")

t = turtle.Turtle()
name = input("Enter your name: ")
num1 = int(input("Enter a number: "))
t.penup()
t.goto(0,180)
t.pendown()
t.pencolor("Red")
t.write(name, font=("arial", 30, "normal"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("blue")
t.write(num1, font=("arial", 30, "normal"),align="center")

turtle.done()