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
    ("http://foundationcenter.org/extension/fcorg/design/fcorg_user/images/fc_logo_orange.png")
a_img_size = [a_img.get_width(), a_img.get_height()]
a_img_center = [a_img_size[0] / 2, a_img_size[1] / 2]
print
a_img_size


# draw handler
def draw(canvas):
    global dest
    if a_img_size[0] > 0 and a_img_size[1] > 0:
        canvas.draw_image(a_img, a_img_center, \
                          a_img_size, dest, a_img_size)


# create frame and register draw handler
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)

# start frame
frame.start()