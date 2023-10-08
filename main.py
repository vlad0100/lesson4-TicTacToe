# Game Tic Tac Toe

def print_table(values):
    print('\n')


    print("\t    |    |")
    print("\t {}   | {}   | {}" .format(values[0], values[1], values[2]))
    print("\t____|____|____")

    print("\t    |    |")
    print("\t {}   | {}   | {}" .format(values[3], values[4], values[5]))
    print("\t____|____|____")

    print("\t    |    |")
    print("\t {}   | {}   | {}" .format(values[6], values[7], values[8]))

    print('\n')

def print_score_board(score_board): #va printa lista de puncte/score
    print("\t________________________________")
    print("\t          Score Board           ")
    print("\t________________________________")

    players = list(score_board.keys())
    print("\t       ", players[0], "\t      ", score_board[players[0]])
    print("\t       ", players[1], "\t      ", score_board[players[1]])

    print("\t_______________________________")


def check_win(player_pos, current_player):
    check = [
        [1,2,3], [4,5,6], [7,8,9],
        [1,4,7], [2,5,8], [3,6,9],
        [1,5,9], [3,5,7]
    ]

    for x in check:
        if all(y in player_pos[current_player] for y in x):
            return True
    return False


def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['0']) == 9:
        return True
    return False

def game(current_player):
    values = ['' for x in range(9)]

    player_pos = {'X': [], '0': []}

    while True:
        print_table(values)

        try:
            print("Player", current_player, "turn.")
            print("Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("wrong data")
            continue
        if move < 1 or move > 9:
            print("Wrong input")
            continue


        if values[move - 1] != '':
            print("Place already filled")
            continue
        values[move - 1] = current_player

        player_pos[current_player].append(move)
        if check_win(player_pos, current_player):
            print_table(values)
            print("Player ", current_player, " has won")
            print("\n")
            return current_player
        if check_draw(player_pos):
            print_table(values)
            print("Game Draw")
            print("\n")
            return 'Draw'

        if current_player == 'X':
            current_player == '0'

        else:
            current_player = 'X'

if __name__ == '__main__':  #'__main__' (se mai poate scrie si asa)
    print("Player 1: ")
    player1 = input("Enter the name ...")
    print("\n")

    print("Player 2: ")
    player2 = input("Enter the name")
    print("\n")

    current_player = player1

    player_choice = {'X': "", '0': ""}


    options = ['X', '0']

    score_board = {player1: 0, player2: 0}
    print_score_board(score_board)

    while True:
        print("Choose X or 0 ...", current_player)
        print("Enter 1 for X")
        print("Enter 2 for 0")
        print("Enter 3 to Quit")

        try:
            choice = int(input())

        except ValueError:
            print("Wrong data type")
            continue
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['0'] = player2
            else:
                player_choice['0'] = player1

        elif choice == 2:
            player_choice['0'] = current_player
            if current_player == player1:
                player_choice['0'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print_score_board(score_board)
            print("Game quit")
            break

        else:
            print("Wrong data")

        winner = game(options[choice - 1])

        if winner != 'Draw':
            player_winner = player_choice[winner]
            score_board[player_winner] = score_board[player_winner] + 1
        if current_player == player1:
            current_player = player2
        else:
            current_player