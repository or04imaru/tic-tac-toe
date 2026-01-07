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

    while True:
        try:
            chosen_cell = int(input("choose: "))
        except ValueError:
            print("what was that?")
            continue

        if chosen_cell < 0 or chosen_cell > 9:
            print("you kidding?")
            continue

        row = (chosen_cell - 1) // 3
        col = (chosen_cell - 1) % 3

        if board[row][col] == "X" or board[row][col] == "O":
            print("Cell already taken")
            continue

        else:
            if all_turns % 2 == 0:
                board[row][col] = "X"
            else:
                board[row][col] = "O"
            all_turns += 1
            break

def checker(board):
    global all_turns
    winner = ""

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            winner = board[row][0]

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column]:
            winner = board[0][column]

    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]

    if all_turns == 9:
        return "nobody"

    return winner

while True:
    input("press enter to play...")
    all_turns = 0
    game_over = False
    game_board = initialize_board()
    show_board(game_board)

    while not game_over:
        players_move(game_board)
        show_board(game_board)

        victor = checker(game_board)
        if victor:
            game_over = True
            print(victor, "is the winner", "\n")