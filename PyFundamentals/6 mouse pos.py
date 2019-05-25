# Echo mouse click in console

###################################################
# Student should enter code below

import simplegui

# define mouseclick handler

def click(pos):
    print "Mouse click at " + str(pos)

# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 300)
frame.set_mouseclick_handler(click)

# start frame
frame.start()


