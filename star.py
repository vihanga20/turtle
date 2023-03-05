import turtle as tu
import colorsys as sy

tu.setup(800,800)
tu.title("Star")
tu.tracer(10)
tu.width(4)
tu.bgcolor("black")

def square(x):
    for i in range(3):
        tu.forward(x)
        tu.left(90)
    tu.forward(x)
for k in range(20):
    for d in range(10):
        tu.color(sy.hsv_to_rgb(d/10,1-k/20,1))
        tu.right(135)
        square(200-k*4)
        tu.right(135)
        tu.circle(50,36)
tu.hideturtle()
tu.done()
