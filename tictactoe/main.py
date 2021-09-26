board = """
    7 |  8 |  9
  ----+----+----
    4 |  5 |  6
  ----+----+----
    1 |  2 |  3
"""

print(board)
moves = ["", "", "", "", "", "", "", "", "", ""]
#index   0    1  2   3    4  5   6   7   8   9
# [""]*9


def display_board():
    global board
    # global = something that is not in the section/ whole code.

    # print out the board
    # reflect moves array to the board
    for x in range(1, 10):
        if moves[x] != "":
            board = board.replace(str(x), moves[x])

    print(board)


display_board()

print("Time to play Tic Tac Toe!")
# Add a player vs player version as well.

rules = "Do you want to know the rules of tic tac toe?[Y]es or [N]o?"
rules_options = "YN"
rules_input = ""

while rules_input not in rules_options or len(rules_input) != 1:
    rules_input = input(rules).upper()

    if rules_input == "Y":
        print("The rules of tic tac toe are that you have to get three in a row and stop the other player from doing "
              "so before you do. The first one to do it wins. If no one gets 3 in a row then it becomes a tie/draw. "
              "You will also need to choose a icon/ X and O. You will have alternating(swapping) turns. You cannot "
              "place in a spot that has already been taken by a X or O. You can't pass a turn or change icons (X or O)." 
              "Press the number on you keyboard of the place you want your icon to take for example, 5.               "
              "                                                                                                       ")
# "Press [D] when done to continue." Add later to make it easier and get rid of spaces at the end.

    elif rules_input == "N":
        pass

print("Choose your icon, X or O, X goes first. Choose X if you want to go first,"
      "but choose O if you want to go second.")

icons = "Would you like [X] or [O]?"
icon_options = "XO"
icon_input = ""

while icon_input not in icon_options or len(icon_input) != 1:
    icon_input = input(icons).upper()

    if icon_input == "X":
        print("")

    elif icon_input == "O":
        print("")
# Next, array. Get array done by next sunday.




def game_init():
    # initialise the game board
    # we need to have a 3x3 array
    # initialise both players -- someone take x, the other take o
    pass


def game_play(is_player):
    # game play engine
    pass


def winning_condition():
    # check the board to see if someone has won
    return False


game_init()
while not winning_condition():
    game_play()
    display_board()
