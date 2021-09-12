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
        print("The rules are that you have to get three in a row and stop the other player from doing so before"
              "you do. The first one to do it wins. You will have alternating(swapping) turns.")