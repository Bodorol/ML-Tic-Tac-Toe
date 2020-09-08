import re


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
        return board[1][1] + " wins"
    for i in range(3):
        if board[i][0] + board[i][1] + board[i][2] in ["XXX", "OOO"]:
            return board[i][0] + " wins"
    for j in range(3):
        if board[0][j] + board[1][j] + board[2][j] in ["XXX", "OOO"]:
            return board[0][j] + " wins"
    for k in range(3):
        if not all([x for x in map(lambda x: x in ["X", "O"], board[k])]):
            return "Game not finished"
    else:
        return "Draw"


startup = list(input("Enter cells: "))
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(startup[j + 3 * i])
    board.append(row)
char = "X" if len([x for x in re.finditer("X", "".join(startup))]) == len(
    [x for x in re.finditer("O", "".join(startup))]) else "O"
display_board(board)
try:
    x, y = map(lambda num: int(num) if num.isdigit() else False, input().split())
except:
    x, y, = False, False
valid = False
while not valid:
    if not (x and y):
        print("You should enter numbers!")
    elif x > 3 or y > 3:
        print("Coordinates should be from 1 to 3!")
    elif board[3 - y][x - 1] in ("X", "O"):
        print("This cell is occupied! Choose another one!")
    else:
        valid = True
        break
    try:
        x, y = map(lambda num: int(num) if num.isdigit() else False, input().split())
    except:
        x, y, = False, False
board[3 - y][x - 1] = char
display_board(board)
print(check_winner(board))
