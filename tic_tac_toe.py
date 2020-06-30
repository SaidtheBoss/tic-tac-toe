# command line tic tac toe made with python 3.8.3
# compatible for python 3.6 and above
# formatted using black
#
#
#
# importing os name and the system function from the os module
from os import system, name

# function for updating the screen
# 1) clears screen
# 2) displays updated tic tac toe board
def screen_update():
    # 1) clearing screen
    # "nt" = Windows
    # "posix" = Unix/MacOS
    if name == "nt":
        # execute the "cls" command if the user OS is windows
        system("cls")
    else:
        # execute the "clear" command if the user OS is Unix/MacOS
        system("clear")
    # 2) printing tic tac toe board
    print("press key corresponding to slot to place X or O")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print("")
    print(
        f"| {variables['spacelist'][2]} | {variables['spacelist'][5]} | {variables['spacelist'][8]} |"
    )
    print(
        f"| {variables['spacelist'][11]} | {variables['spacelist'][14]} | {variables['spacelist'][17]} |"
    )
    print(
        f"| {variables['spacelist'][20]} | {variables['spacelist'][23]} | {variables['spacelist'][26]} |"
    )


# function for updating the tic tac toe board
# 1) takes user input
# 2) validates the user input
# 3) places X or O corresponding to the user input
# 4) checks for a win after each turn
def board_update():
    # 1) taking user input
    if variables["input_counter"] % 2 == 0:
        char = "X"
    else:
        char = "O"
    choice = input(f"place {char}(1-9): ")
    # 2) input validation
    if choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        variables["input_counter"] += 1
        index = 0
        # 3) assigning X or O to corresponding slot if user input is valid
        for _ in range(int(choice) * 3):
            if (
                int(choice) == variables["spacelist"][index]
                and variables["spacelist"][index + 1] == True
            ):
                variables["spacelist"][index + 1] = False
                if variables["p2_input_lock"] == False:
                    variables["spacelist"][index + 2] = char
                else:
                    variables["spacelist"][index + 2] = "X"
                screen_update()
                break
            index += 1
        else:
            screen_update()
            print(f"there is already a 'X' or 'O' at: {choice}")
            board_update()
    else:
        screen_update()
        print(f"invalid choice: {choice}")
        board_update()
    # 4) checking for all possible win conditions
    index = 2
    for _ in range(3):
        # checking for all possible wins horizontally
        # check for X
        if (
            variables["spacelist"][index] == "X"
            and variables["spacelist"][index + 3] == "X"
            and variables["spacelist"][index + 6] == "X"
        ):
            variables["game_status"] = False
            print("X wins!")
            break
        # check for O
        elif (
            variables["spacelist"][index] == "O"
            and variables["spacelist"][index + 3] == "O"
            and variables["spacelist"][index + 6] == "O"
        ):
            variables["game_status"] = False
            print("O wins!")
            break
        index += 9
    else:
        # if all horizontal win conditions are false
        # check for all possible wins vertically
        index = 2
        for _ in range(3):
            # check for X
            if (
                variables["spacelist"][index] == "X"
                and variables["spacelist"][index + 9] == "X"
                and variables["spacelist"][index + 18] == "X"
            ):
                variables["game_status"] = False
                print("X wins!")
                break
            # check for O
            elif (
                variables["spacelist"][index] == "O"
                and variables["spacelist"][index + 9] == "O"
                and variables["spacelist"][index + 18] == "O"
            ):
                variables["game_status"] = False
                print("O wins!")
                break
            index += 3
        else:
            # if all horizontal and vertical win conditions are false
            # check for diagonal win conditions
            if variables["spacelist"][14] in ("X", "O"):
                # check for X
                if (
                    variables["spacelist"][2] == "X"
                    and variables["spacelist"][26] == "X"
                ):
                    variables["game_status"] = False
                    print("X wins!")
                elif (
                    variables["spacelist"][8] == "X"
                    and variables["spacelist"][20] == "X"
                ):
                    variables["game_status"] = False
                    print("X wins!")
                # check for O
                elif (
                    variables["spacelist"][2] == "O"
                    and variables["spacelist"][26] == "O"
                ):
                    variables["game_status"] = False
                    print("O wins!")
                elif (
                    variables["spacelist"][8] == "O"
                    and variables["spacelist"][20] == "O"
                ):
                    variables["game_status"] = False
                    print("O wins!")


# game loop
while True:
    # defining all the variables required
    variables = {
        "spacelist": [
            1,
            True,
            " ",
            2,
            True,
            " ",
            3,
            True,
            " ",
            4,
            True,
            " ",
            5,
            True,
            " ",
            6,
            True,
            " ",
            7,
            True,
            " ",
            8,
            True,
            " ",
            9,
            True,
            " ",
        ],
        "input_counter": 0,
        "p2_input_lock": False,
        "game_status": True,
    }
    # running the game
    while variables["game_status"] == True:
        screen_update()
        for _ in range(8):
            board_update()
            if variables["game_status"] == False:
                break
        # if the game did not end within first 8 turns
        else:
            variables["p2_input_lock"] = True
            board_update()
            break
    # asking user if they want to continue playing
    while True:
        # taking user input
        choice = input("continue playing?(0/1): ")
        # validating user input
        if choice in ("0", "1"):
            break
        else:
            screen_update()
            print(f"invalid input: {choice}")
    # stop game if user input is 0 , else restart
    if choice == "0":
        print("thank you for playing!")
        break

