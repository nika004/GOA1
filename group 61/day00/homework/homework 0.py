from turtle import*
#We want to paint a house

#Step 1: draw a square
shape("turtle")
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#End of square

#Door
forward(70)
color("yellow")
left(90)
forward(120) #Height of the door
right(90)
forward(60)
right(90)
forward(120)
#End of door

#Roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#End of roof

#Windows
left(30)
forward(10)

color("blue")
begin_fill()
left(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
end_fill()

penup()
goto(200,190)
pendown()

color("blue")
begin_fill()
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
end_fill()
#End of windows

exitonclick()