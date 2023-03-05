import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(5000)

draw_circle(tommy, "yellow", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "red", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.speed(5000)
tommy.write("Turtle module in Python!", align="center", font=(None, 16, "bold"))
tommy.color('red')
tommy.goto(0,-80)
