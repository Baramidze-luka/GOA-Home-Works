from turtle import *

#we want to paint a house
#setp 1: draw a squear
width(7)



color("purple")

begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#end of squear


#start paint a door
forward(70)

color("yellow")
begin_fill()
left(90)


forward(120)
right(90)

forward(60)
right(90)

forward(120)
left(90)
end_fill()

#end paint a door
color("red")
penup()
goto(200,200)
pendown()
begin_fill()
right(90)
right(150)
forward(200)

left(120)
forward(200)
end_fill()
#draw a windows
color("blue")
begin_fill()
left(30)
forward(80)

left(90)
forward(70)

left(90)
forward(80)

left(90)
forward(70)
end_fill()

#end draw a one window

#start draw another window
begin_fill()
penup()
goto(200,200)
pendown()

forward(70)
left(90)

forward(80)
left(90)

forward(70)
left(90)

forward(80)
end_fill()

#draw a 

color("gray")

begin_fill()

forward(50)
left(90)

forward(10)
left(90)

forward(50)

end_fill()

penup()
goto(200,0)
pendown()

color("green")
begin_fill()

left(90)
forward(100)

right(90)
forward(200)

right(90)
forward(400)

right(90)
forward(200)

right(90)
forward(100)

end_fill()



exitonclick()