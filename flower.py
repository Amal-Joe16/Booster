import turtle
num_petals = int(input("Enter the number of petals for the flower: "))
screen = turtle.Screen()
t = turtle.Turtle()
for _ in range(num_petals):
    t.begin_fill()
    for _ in range(2):
        t.circle(100, 60)
        t.left(120)
    
    t.left(360 / num_petals)
t.hideturtle()
screen.mainloop()