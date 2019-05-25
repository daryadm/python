# Ball motion with an implicit timer

import simplegui

# Initialize globals
p_pos = [10, 20]
p_change = [3, 0.7]


# define event handlers
def timer_handler():
    p_pos[0] += p_change[0]
    p_pos[1] += p_change[1]


def draw(canvas):
    # Draw point
    canvas.draw_point(p_pos, "Red")
    canvas.draw_polygon([[50, 50], [180, 50], [180, 140], [50, 140]], 1, "Green")


# create frame
frame = simplegui.create_frame("Point and rectangle", 400, 400)
timer = simplegui.create_timer(500, timer_handler)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
timer.start()