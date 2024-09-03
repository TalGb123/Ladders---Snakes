import random
import time
from colorama import Fore, init

init(autoreset=True)


def initialize(board):
    i = 1
    for row in range(10):
        row_to_add = []
        for col in range(10):
            row_to_add.append(str(i))
            i += 1

        board.append(row_to_add)
    board[0][3] = board[6][1] = board[7][5] = board[3][7] = board[8][7] = '🪜1'
    board[1][6] = board[3][4] = board[2][9] = board[6][6] = '🪜2'
    board[4][5] = board[5][8] = board[1][1] = '🪜3'
    board[2][1] = board[5][8] = "🪜4"

    board[1][4] = board[7][2] = board[8][5] = board[9][8] = '🐍1'
    board[2][7] = board[4][5] = board[7][7] = '🐍2'
    board[4][5] = board[3][3] = '🐍3'
    board[9][1] = board[8][2] = '🐍4'
    return board


def print_board(board):
    print("\n-------------------------------------------------------------")
    for row in range(len(board) - 1, -1, -1):
        for col in range(0, len(board[row]), 1):
            if row == 9:
                if col == 9:
                    print(" ", board[row][col], end='|')
                else:
                    print(" ", board[row][col], end=' |')
            elif row == 0:
                if col == 0:
                    print(" ", board[row][col], end=' |')
                else:
                    print(" ", board[row][col], end='  |')
            else:
                print(" ", board[row][col], end=' |')

        print("\n-------------------------------------------------------------")


def roll_dice():
    minimum = 1
    maximum = 6
    game_over = False
    while not game_over:
        print("Rolling the dices...")
        time.sleep(0.5)
        print("The values are....")
        time.sleep(1)
        dice = random.randint(minimum, maximum)
        return dice


def move_player(dice_roll, player, p1, p2, board, default_board):
    if player == 1:
        if (p1[0] == 9) and (p1[1] + dice_roll >= 10):
            return board, player
    else:
        if (p2[0] == 9) and (p2[1] + dice_roll >= 10):
            return board, player

    for move in range(1, dice_roll + 1):
        if player == 1:
            if p1[1] + 1 == 10:
                p1[0] = p1[0] + 1
                p1[1] = 0
            elif 9 >= p1[1] >= 0:
                p1[1] = p1[1] + 1
        else:
            if p2[1] + 1 == 10:
                p2[0] = p2[0] + 1
                p2[1] = 0
            elif 9 >= p2[1] >= 0:
                p2[1] = p2[1] + 1
    ladder_check(default_board, p1, p2)
    snake_check(default_board, p1, p2)
    return board, player


def marking_place(player, board, p1, p2, count, color1, color2):
    if player == 1:
        if count != 0:
            if board[p1[0]][p1[1]] == board[p2[0]][p2[1]]:
                board[p2[0]][p2[1]] = (color1 + "p1") + (Fore.LIGHTWHITE_EX + "+") + (color2 + "p2")
            else:
                board[p1[0]][p1[1]] = color1 + "p1"
        else:
            board[p1[0]][p1[1]] = color1 + "p1"
    else:
        if board[p1[0]][p1[1]] == board[p2[0]][p2[1]]:
            board[p2[0]][p2[1]] = (color1 + "p1") + (Fore.LIGHTWHITE_EX + "+") + (color2 + "p2")
        else:
            board[p2[0]][p2[1]] = color2 + "p2"


def clear_steps(player, board, default_board, p1, p2, color1, color2):
    if player == 1:
        if board[p1[0]][p1[1]] == board[p2[0]][p2[1]]:
            board[p1[0]][p1[1]] = color2 + "p2"
        else:
            board[p1[0]][p1[1]] = default_board[p1[0]][p1[1]]
    elif player == 2:
        if board[p1[0]][p1[1]] == board[p2[0]][p2[1]]:
            board[p2[0]][p2[1]] = color1 + "p1"
        else:
            board[p2[0]][p2[1]] = default_board[p2[0]][p2[1]]


def snake_check(default_board, p1, p2):
    if p1[1] <= 9:
        if default_board[p1[0]][p1[1]][0] == "🐍":
            assistance = int(default_board[p1[0]][p1[1]][1])
            p1[0] -= assistance
    if p2[1] <= 9:
        if default_board[p2[0]][p2[1]][0] == "🐍":
            assistance = int(default_board[p2[0]][p2[1]][1])
            p2[0] -= assistance
    return p1, p2


def ladder_check(default_board, p1, p2):
    if p1[1] <= 9:
        if default_board[p1[0]][p1[1]][0] == "🪜":
            assistance = int(default_board[p1[0]][p1[1]][1])
            p1[0] += assistance
    if p1[1] <= 9:
        if default_board[p2[0]][p2[1]][0] == "🪜":
            assistance = int(default_board[p2[0]][p2[1]][1])
            p2[0] += assistance
    return p1, p2


def switch_player(var):
    if var == 1:
        player = 1
        var = 2
    else:
        player = 2
        var = 1
    return player, var


def main():
    color_dict = {"o": Fore.YELLOW,
                  "g": Fore.GREEN,
                  "r": Fore.RED,
                  "b": Fore.BLUE,
                  "m": Fore.MAGENTA,
                  "w": Fore.LIGHTWHITE_EX,
                  "y": Fore.LIGHTYELLOW_EX}
    count = 0
    player = 1
    game_over = False
    p1 = [0, 0]
    p2 = [0, 0]
    var = 2
    print(Fore.LIGHTBLUE_EX + """----------------------------------
| Welcome to snakes and ladders! |
| Let's pick your colors!        |
----------------------------------""")
    player_color1 = input(f"""Choose the color for player 1:
    {Fore.YELLOW + "o = orange"}
    {Fore.GREEN + "g = green"}
    {Fore.RED +"r = red"}
    {Fore.BLUE + "b = blue"}
    {Fore.MAGENTA + "m = magenta"}
    {Fore.LIGHTWHITE_EX + "w = white"}
    {Fore.LIGHTYELLOW_EX + "y = yellow"}
    {Fore.LIGHTWHITE_EX + "color -"} """)
    print()
    player_color2 = input(f"""Choose the color for player 2:
    {Fore.YELLOW + "o = orange"}
    {Fore.GREEN + "g = green"}
    {Fore.RED +"r = red"}
    {Fore.BLUE + "b = blue"}
    {Fore.MAGENTA + "m = magenta"}
    {Fore.LIGHTWHITE_EX + "w = white"}
    {Fore.LIGHTYELLOW_EX + "y = yellow"}
    {Fore.LIGHTWHITE_EX + "color -"} """)
    color1 = color_dict[player_color1]
    color2 = color_dict[player_color2]

    board = initialize([])
    default_board = initialize([])
    print_board(board)
    while not game_over:
        print(f"player {player if count == 0 else player[0]} turn's to play!!!")
        while True:
            is_ready = input("Are you ready to play? Press enter ")
            if is_ready == "":
                break
        dice_roll = roll_dice()
        print(dice_roll)
        if count == 0 or count == 1:
            move = move_player(dice_roll - 1, player, p1, p2, board, default_board)
            marking_place(player, board, p1, p2, count, color1, color2)
        else:
            clear_steps(player[0], board, default_board, p1, p2, color1, color2)
            move = move_player(dice_roll, player[0], p1, p2, board, default_board)
            marking_place(player[0], board, p1, p2, count, color1, color2)
        print_board(move[0])
        count += 1
        if (p1[0] == 9 and p1[1] == 9) or (p2[0] == 9 and p2[1] == 9):
            game_over = True
            print(f"player {player[0]} has won, good game.")
            print(f"it took {(count // 2) + 1} moves! ")
        player = switch_player(var)
        var = player[1]


main()