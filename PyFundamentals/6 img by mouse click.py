# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
dest = [WIDTH / 2, HEIGHT / 2]

# load test image
a_img = simplegui.load_image \
    ("http://commondatastorage.googleapis.com\
/codeskulptor-assets/asteroid.png")
a_img_size = [95, 93]
a_img_center = [a_img_size[0] / 2, a_img_size[1] / 2]


# mouseclick handler
def click(pos):
    global dest
    dest = [pos[0], pos[1]]


# draw handler
def draw(canvas):
    global dest
    canvas.draw_image(a_img, a_img_center, \
                      a_img_size, dest, a_img_size)


# create frame and register draw handler
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()