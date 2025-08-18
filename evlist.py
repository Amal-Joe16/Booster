import time
import datetime as dt
import turtle

t = turtle.Turtle()
t1 = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")


t1.pensize(3)
t1.color('red')
t1.penup()
t1.goto(-20, 0)
t1.pendown()

for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)

t1.hideturtle()

while True:
    now = dt.datetime.now()  
    sec = now.second
    min = now.minute
    hr = now.hour

    
    if hr > 12:
        hr -= 12
    if hr == 0:
        hr = 12

    t.hideturtle()
    t.clear()

    
    t.color("red")
    t.goto(-20, 10)  
    t.write(str(hr).zfill(2) + ":" + str(min).zfill(2) + ":" + str(sec).zfill(2),
            font=("Arial Narrow", 35, "bold"))

    
    t.color("red")
    day_str = now.strftime("%A, %B %d, %Y")  
    t.goto(-20, -40)
    t.write(day_str, font=("Arial Narrow", 18, "normal"))

    time.sleep(1)




