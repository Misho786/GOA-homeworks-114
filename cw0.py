from turtle import *


speed(15)

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
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)


forward(120)  #height of door
right(90)

forward(60)
right(90)
forward(120)

 #door done

#making roof

penup()
goto(200, 200)

pendown()

color("blue")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

# making window
color("brown")
penup()
goto(10, 70)
setheading(0)
pendown()
# making second window
color("brown")
for i in range(4):
    forward(50)
    left(90)

penup()
goto(140, 70)
setheading(0)
pendown()

for i in range(4):
    forward(50)
    left(90)



exitonclick()