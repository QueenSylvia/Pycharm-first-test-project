print("    |    |   "
      "----|----|---"
      "----|----|---"
      "    |    |   "
      "             "
      "X ALWAYS GOES FIRST")

rules = "Do you want to know the rules?[Y]es or [N]o?"
rules_option = "YN"
rules_input = ""

while rules_input not in rules_option or len(rules_input) != 1:
    rules_input = input(rules).upper()

    if rules_input == "Y":
        print("The rules are that you have to get three in a row and stop the other player from doing so before "
              "you do. The first one to do it wins. You will have alternating(swapping) turns.")
    elif rules_input == "N":
        pass


def display_board():
    # print out the board
    print("    |    |   "
          "----|----|---"
          "----|----|---"
          "    |    |   "
          "             ")


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
