from random import randint

board = []
turns = 0

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))





def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)
board[ship_row][ship_col] = "S"
print_board(board)

for turn in range(5):

    turns += 1
    guess_row = int(input("Guess Row: ")) - 1
    guess_rowpr = guess_row + 1
    print("You entered " + str(guess_rowpr))
    guess_col: int = int(input("Guess Col: ")) - 1
    guess_colpr = guess_col + 1
    print("You entered " + str(guess_colpr))

    # Write your code below!
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    elif guess_row not in range(0, len(board)) or \
         guess_col not in range(0, len(board[0])):
        print("Oops, that's not even in the ocean.")
        if turns == 4:
            print("Game over")
    elif board[guess_row][guess_col] == "X":
        print("You guessed that one already.")
        if turns == 4:
            print("Game over")
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)
        if turns == 4:
            print("Game over")

    print("You made " + str(turns) + " turns of 4")




