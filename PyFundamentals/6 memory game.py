# implementation of card game - Memory

import simplegui
import random

deck = list(range(8) * 2)
exposed = list([False] * 16)

# exposed[0] = True
# exposed[1] = True

point_list = [[0, 0], [50, 0], [50, 100], [0, 100]]
turns = 0
state = 0
deck_sh = random.shuffle(deck)


# helper function to initialize globals
def new_game():
    global state, turns, exposed, deck
    random.shuffle(deck)
    exposed = list([False] * 16)
    state = 0
    turns = 0
    label.set_text("Turns: " + str(turns))


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, deck, clicked, exposed, turns, \
        first_card_i, second_card_i, first_card, second_card
    clicked = pos[0] // 50  # index of clicked card

    if state == 0:
        first_card = deck[clicked]  # value of the first clicked card
        exposed[clicked] = True
        first_card_i = clicked
        state = 1
    elif state == 1:
        if exposed[clicked] == False:
            second_card = deck[clicked]
            exposed[clicked] = True
            second_card_i = clicked
            state = 2

        else:
            pass
    elif state == 2:

        if exposed[clicked] == False:
            turns += 1
            if first_card == second_card:
                exposed[first_card_i] = True
                exposed[second_card_i] = True
                first_card = deck[clicked]

            else:
                exposed[first_card_i] = False
                exposed[second_card_i] = False
                first_card = deck[clicked]

        else:
            pass
        exposed[clicked] = True
        first_card_i = clicked
        state = 1
        label.set_text("Turns: " + str(turns))
    else:
        print
        "mouseclick malfunctioned"


# cards are logically 50x100 pixels in size
def draw(canvas):
    global exposed, deck
    point = [0, 75]

    for i in range(len(exposed)):
        card = deck[i]
        if exposed[i] == True:
            canvas.draw_text(str(card), point, 100, "Red")
        else:
            point_list = [[point[0], 0], [point[0] + 50, 0], [point[0] + 50, 100], [point[0], 100]]
            canvas.draw_polygon(point_list, 2, "White", "Blue")
        point[0] += 50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns: 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric