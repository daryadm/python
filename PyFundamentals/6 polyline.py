# Polyline drawing problem

###################################################
# Student should enter code below

import simplegui
import math

polyline = []


# define mouseclick handler
def click(pos):
    global polyline
    polyline.append(pos)


# button to clear canvas
def clear():
    global polyline
    polyline = []


# define draw
def draw(canvas):
    global polyline
    if len(polyline) == 1:
        canvas.draw_point(polyline[0], 'Green')
    else:
        for i in range(len(polyline) - 1):
            canvas.draw_line(polyline[i], polyline[i + 1], 2, 'Red')


# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()
