import turtle

turtle.bgcolor("green") #back ground eke paata
turtle.title("Nayana & Amara") #title eka

nayana = turtle.Turtle() #adura ganna leesi wena namak damme
amara = turtle.Turtle() #adura ganna leesi wena namak damme

nayana.color('red') #kotuwa athula pata wena color eka
amara.color('green')

nayana.shape('turtle')
amara.shape('turtle')

turtle.speed(50)

nayana.begin_fill()
nayana.goto(400,0)
nayana.goto(400,-400)
nayana.goto(-400,-400)
nayana.goto(-400,0)
nayana.goto(0,0)
nayana.end_fill()


turtle.speed(100)
amara.penup()
amara.color('black') #text color eka
amara.goto(-70,100)
amara.write("nayana me salgahk needa", font=("Arial", 16, "normal"))
amara.goto(0,50)
amara.pendown()

turtle.speed(100)
nayana.penup()
nayana.color('black') #text color eka
nayana.goto(-40,-100)
nayana.write("Ow amara me sal gahak", font=("Arial", 16, "normal"))
nayana.goto(0,-130)
nayana.pendown()

turtle.hideturtle()
turtle.done()
