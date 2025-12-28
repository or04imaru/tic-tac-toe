
def initialize_board():
    return [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

def show_board(board):
    for row in board:
        print(*row)
    print("")

def players_move(board):
    global all_turns

    try:
        chosen_cell = int(input("choose: "))
        if chosen_cell < 0 or chosen_cell > 9:
            print("you kidding?")
            players_move(board)

        for i in range(3):
            for j in range(3):
                if board[i][j] == chosen_cell:
                    if all_turns % 2 == 1:
                        board[i][j] = "O"
                        all_turns += 1
                    else:
                        board[i][j] = "X"
                        all_turns += 1

    except ValueError:
        print("what was that?")
        players_move(board)

def checker(board):
    global all_turns

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            winner = board[row][0]
            return winner

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column]:
            winner = board[0][column]
            return winner

    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        return winner
    elif board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        return winner

    if all_turns == 9:
        return "nobody"



while True:
    input("press enter to play...")
    all_turns = 0
    game_over = False
    board = initialize_board()
    show_board(board)

    while not game_over:
        players_move(board)
        show_board(board)

        winner = checker(board)
        if winner:
            game_over = True
            print(winner, "is the winner", "\n")