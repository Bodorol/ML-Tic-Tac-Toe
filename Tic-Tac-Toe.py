import random


def display_board(board):
    print("---------")
    for row in board:
        print("| ", end="")
        for piece in row:
            print(piece + " " if piece in ["X", "O"] else "  ", end="")
        print("|")
    print("---------")


def check_winner(board):
    if board[0][0] + board[1][1] + board[2][2] in ["XXX", "OOO"] or board[2][0] + board[1][1] + board[0][2] in ["XXX", "OOO"]:
        return board[1][1]
    for i in range(3):
        if board[i][0] + board[i][1] + board[i][2] in ["XXX", "OOO"]:
            return board[i][0]
    for j in range(3):
        if board[0][j] + board[1][j] + board[2][j] in ["XXX", "OOO"]:
            return board[0][j]
    for k in range(3):
        if not all([x for x in map(lambda x: x in ["X", "O"], board[k])]):
            return None
    else:
        return "Draw"


board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]
turn = 0
while check_winner(board) not in ["X", "O", "Draw"]:
    display_board(board)
    if turn == 0:
        try:
            x, y = map(lambda num: int(num) if num.isdigit() else False, input("Enter the coordinates: ").split())
        except:
            x, y, = False, False
        while True:
            if not (x and y):
                print("You should enter numbers!")
            elif x > 3 or y > 3:
                print("Coordinates should be from 1 to 3!")
            elif board[3 - y][x - 1] in ("X", "O"):
                print("This cell is occupied! Choose another one!")
            else:
                break
            try:
                x, y = map(lambda num: int(num) if num.isdigit() else False, input("Enter the coordinates: ").split())
            except:
                x, y, = False, False
        board[3 - y][x - 1] = "X"
    else:
        print('Making move level "easy"')
        x, y = random.randint(1, 3), random.randint(1, 3)
        while board[3 - y][x - 1] in ("X", "O"):
            x, y = random.randint(1, 3), random.randint(1, 3)
        board[3 - y][x - 1] = "O"
    turn = (turn + 1) % 2
    display_board(board)
print(check_winner(board) + " wins" if check_winner(board) in ["X", "O"] else "Draw")