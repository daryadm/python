# Simple "screensaver" program.

# Import modules
import simplegui
import random

# Global state
message = "Python is Fun!"
position = [50, 50]
width = 500
height = 500
interval = 2000

# Handler for text box
def update(text):
    global message
    message = text

# Handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")

# Create a frame
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text = frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()
timer.start()
--------------------------------------------------------------------
# Counter ticks

###################################################
# Student should add code where relevant to the following.

import simplegui

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)
timer.start()
------------------------------------------------------------------------
# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1

# Event handlers for buttons
def start():
    timer.start()

def stop():
    timer.stop()

def reset():
    global counter
    counter = 0


# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
timer = simplegui.create_timer(1000, tick)

# Start timer
frame.start()
timer.start()
----------------------------------------------------------------------
# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui

color = "Red"
def change_color():
    global color
    if color == "Red":
        color = "Blue"
    elif color == "Blue":
        color = "Red"
    return color

# Timer handler
def tick():
    change_color()
    frame.set_canvas_background(color)


# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()

# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui

color = "Red"


# Timer handler
def tick():
    global color
    if color == "Red":
        color = "Blue"
    else:
        color = "Red"
    frame.set_canvas_background(color)

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.set_canvas_background(color)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()
--------------------------------------------------------------------------
# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def tick():
    global radius
    radius += 1

# Draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], radius, 1, "White", "White")

# Create frame and timer
frame = simplegui.create_frame("Expanding circle", 200, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# Start timer
frame.start()
timer.start()
------------------------------------------------------------------------------
# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks
    total_ticks += 1

# Button handler
def click():
    global total_ticks, first_click
    if first_click:
        first_click = False
        total_ticks = 0
        timer.start()
    else:
        first_click = True
        timer.stop()
        print "Time between clicks is " + str(total_ticks / 100.0) + " seconds"
        total_ticks = 0

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
