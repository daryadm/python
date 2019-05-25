# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
x = 0
y = 0
running = False
score = str(x) + "/" + str(y)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    A = t // 600
    B = t // 10 % 60 // 10
    C = t // 10 % 60 % 10
    D = t % 10
    time = str(A) + ":" + str(B) + str(C) + "." + str(D)
    return t, time


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True
    return running


def stop():
    timer.stop()
    global y, x, score, t, running
    if running != False:
        y +=1
    else: y

    if running != False and t % 10 == 0 :
        x +=1
    else: x
    score = str(x) + "/" + str(y)
    running = False
    return score, x, y, running

def reset():
    global t, x, y, score
    running = False
    timer.stop()
    t = 0
    x = 0
    y = 0
    score = str(x) + "/" + str(y)
    return score, x, y


# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t +=1
    print t



# define draw handler
def draw(canvas):
    format(t)
    canvas.draw_text(time, [150,200], 36, "Blue")
    canvas.draw_text(score, [320,20], 24, "Green")


# create frame
frame = simplegui.create_frame("Stop watch", 400, 400)
timer = simplegui.create_timer(100, tick)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)


# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
