#dist between a point and a circle
import math
p = [4,7]
c = [2,9]
r = 2

d = math.sqrt((p[0] - c[0])**2 + (p[1] - c[1])**2) - r
print d

#######################################

import simplegui

# Initialize globals
var = 5
message = var


# define event handlers

def keydown(key):
    global var, message
    if key == simplegui.KEY_MAP['up']:
        var = var * 2

        message = var

    return message


def keyup(key):
    global var, message
    if key == simplegui.KEY_MAP['up']:
        var = var - 3
        message = var

    return message


def draw(canvas):
    canvas.draw_text(str(message), [200, 112], 42, "Blue")


# create frame
frame = simplegui.create_frame("global var", 400, 400)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
#################################################################
# Space ship motion

import simplegui

# Initialize globals
p_pos = [0, 0]
time = 2
vel = [0, 0]
acc = [0, 0]
vec = [0.1, 0.5]


# define event handlers
def keydown(key):
    global acc, vec
    if key == simplegui.KEY_MAP['up']:
        acc[0] += vec[0]
        acc[1] += vec[1]


def keyup(key):
    global acc
    if key == simplegui.KEY_MAP['up']:
        acc[0] = acc[0]
        acc[1] = acc[1]


def tick1():
    global vel, time, acc, p_pos
    vel[0] += time * acc[0]
    vel[1] += time * acc[1]
    p_pos[0] += time * vel[0]
    p_pos[1] += time * vel[1]


def draw(canvas):
    # Draw spaceship
    canvas.draw_circle(p_pos, 2, 2, "Blue")


# create frame
frame = simplegui.create_frame("Spaceship motion", 400, 400)
timer = simplegui.create_timer(1000, tick1)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
timer.start()
##################################################################