# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
my_deck = []
player_h = []
dealer_h = []
# player_h_pos = [100, 500]
# dealer_h_pos = [100, 50]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print
            "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        hand_t = ""
        for i in range(len(self.hand)):
            hand_t += str(self.hand[i]) + " "
        return "Hand: " + hand_t

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        self.hand_value = 0
        for card in self.hand:
            self.hand_value += VALUES[str(card.get_rank())]
        for card in self.hand:
            if card.get_rank() == 'A' and self.hand_value + 10 <= 21:
                self.hand_value += 10
            else:
                self.hand_value
        return self.hand_value

        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] = pos[0] + CARD_SIZE[0] + 1


# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                card = Card(s, r)
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(-1)

    def __str__(self):
        deck_t = ""
        for i in range(len(self.deck)):
            deck_t += str(self.deck[i]) + " "
        return "Deck: " + deck_t


# define event handlers for buttons
def deal():
    global outcome, in_play, my_deck, player_h, dealer_h, score
    my_deck = Deck()
    my_deck.shuffle()
    player_h = Hand()
    dealer_h = Hand()
    player_h.add_card(my_deck.deal_card())
    dealer_h.add_card(my_deck.deal_card())
    player_h.add_card(my_deck.deal_card())
    dealer_h.add_card(my_deck.deal_card())
    #    print "Player_" + str(player_h), "Dealer_" + str(dealer_h)
    print
    player_h.get_value()
    if in_play:
        outcome = "You have lost the round. New deal?"
        print
        outcome
        score -= 1
        in_play = False
    else:
        in_play = True
        outcome = "Hit or stand?"


def hit():
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global outcome, in_play, player_h, score, dealer_h
    if in_play == True:
        player_h.add_card(my_deck.deal_card())
        player_h.get_value()
        print
        player_h.get_value()
        print
        "Player_" + str(player_h), "Dealer_" + str(dealer_h)
        if player_h.get_value() > 21:
            outcome = "You have busted. New deal?"
            print
            outcome
            in_play = False
            score -= 1
        print
        score
    else:
        pass


def stand():
    global in_play, dealer_h, outcome, score
    if in_play == False:
        print
        "Reminding you that you have busted"
    else:
        #        print dealer_h, dealer_h.get_value()
        #        dealer_h.add_card(my_deck.deal_card())
        #        dealer_h.get_value()
        #        print dealer_h, dealer_h.get_value()
        while dealer_h.get_value() <= 17:
            dealer_h.add_card(my_deck.deal_card())
            print
            dealer_h, dealer_h.get_value()

        if dealer_h.get_value() > 21:
            outcome = "You have won, because he had busted! New deal?"
            score += 1
            in_play = False
        else:
            if player_h.get_value() > dealer_h.get_value():
                outcome = "You have won by value! New deal?"
                score += 1
                in_play = False
            else:
                outcome = "You have lost! New deal?"
                score -= 1
                in_play = False
        print
        outcome, score

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score


# draw handler
def draw(canvas):
    global player_h, outcome, in_play
    player_h.draw(canvas, [100, 500])
    dealer_h.draw(canvas, [100, 50])
    canvas.draw_text(outcome, [100, 300], 24, 'Black')
    canvas.draw_text('Blackjack', [250, 30], 24, 'Black')
    if not in_play:
        pass

    else:
        canvas.draw_image(card_back, \
                          CARD_BACK_CENTER, \
                          CARD_BACK_SIZE, \
                          (100 + CARD_BACK_SIZE[0] / 2, \
                           50 + CARD_BACK_SIZE[1] / 2), \
                          CARD_BACK_SIZE)
    canvas.draw_text("SCORE: " + str(score), [250, 350], 24, "Red")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric