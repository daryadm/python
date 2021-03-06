# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
counterR = 0
counterL = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [1, 1]
    ball_vel = [(random.randrange(120, 240)) / 60, -(random.randrange(60, 180)) / 60]
    if direction == RIGHT:
        ball_vel[0] = ball_vel[0]

    elif direction == LEFT:
        ball_vel[0] = -ball_vel[0]


#    return ball_pos, ball_vel


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, counterR, counterL  # these are ints
    counterR = 0
    counterL = 0
    spawn_ball(RIGHT)

    paddle1_pos = (HEIGHT - PAD_HEIGHT) / 2
    paddle2_pos = (HEIGHT - PAD_HEIGHT) / 2
    paddle1_vel = 0
    paddle2_vel = 0


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos
    global ball_pos, ball_vel, paddle1_vel, paddle2_vel
    global counterR, counterL

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "Red")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "Blue")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif (ball_pos[1] > paddle1_pos and ball_pos[1] <
          paddle1_pos + PAD_HEIGHT and ball_pos[0] <=
          PAD_WIDTH + BALL_RADIUS or ball_pos[1] >
          paddle2_pos and ball_pos[1] < paddle2_pos +
          PAD_HEIGHT and ball_pos[0] >= WIDTH -
          PAD_WIDTH - BALL_RADIUS):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] = ball_vel[0] * 1.1
        ball_vel[1] = ball_vel[1] * 1.1

    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        spawn_ball(RIGHT)
        counterR += 1
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        spawn_ball(LEFT)
        counterL += 1

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "Gray")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel <= HEIGHT - PAD_HEIGHT and paddle1_pos + paddle1_vel > 0:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel <= HEIGHT - PAD_HEIGHT and paddle2_pos + paddle2_vel > 0:
        paddle2_pos += paddle2_vel
        # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH,
                                                     paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "Red")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos],
                     [WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "Blue")

    # determine whether paddle and ball collide

    # draw scores
    canvas.draw_text("Bluee : " + str(counterR), [(WIDTH / 2 + WIDTH / 6), (HEIGHT / 12)], 24, "Blue")
    canvas.draw_text("Redya : " + str(counterL), [(WIDTH / 6), (HEIGHT / 12)], 24, "Red")


def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 3
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 3
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 3
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 3


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


def restart():
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart0 = frame.add_button("Restart", restart, 100)

# start frame
new_game()
frame.start()
