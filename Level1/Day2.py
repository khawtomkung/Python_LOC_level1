# Turtle library

import turtle

"""
turtle._

# Move turtle forward and backward for number of pixel
forward(distance)
backward(distance)

# Turn turtle for a particular degree
left(angle)
right(angle)

# tell/change color of the line (and also the fill)
bgcolor(color_name_or_hex)
color(color_name_or_hex)
color(color_of_line, color_of_fill)

# turtle screen will autumetically closed after the run, to make it
# still, use
mainloop() # or
done() # at the end.

# set the width of the line
width(number)
# hide the turtle (and speed up the drawing a little bit)
hideturtle()
# set the speed from 0 to 10
speed(number)

# if pen is up, then there is no drawing
penup()
pendown()
# check if the pen is currently down
isdown()

# The duo is use to fill the shape turtle created.
begin_fill()
end_fill()

# this gives you a literal turtle.
turtle.shape("turtle")

# move turtle to a specific position (it start at (0, 0))
goto(x, y)
# check current position
position()
# move turtle to the origin
home()

# draw a circle
circle(radius, angle_of_arc)

# Write string at the turtle position
write(arg, move=False, align='left', font=('Arial', 8, 'normal'))

for _ in range():
    turtle._()
"""
