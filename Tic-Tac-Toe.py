import random
import sys

class Player:

    def __init__(self, move, board, piece):
        self.move = move
        self.board = board
        self.piece = piece

    def make_move(self):
        self.move(self)


def easy_move(player: Player):
    print('Making move level "easy"')
    x, y = random.randint(1, 3), random.randint(1, 3)
    while player.board[3 - y][x - 1] in ("X", "O"):
        x, y = random.randint(1, 3), random.randint(1, 3)
    player.board[3 - y][x - 1] = player.piece


def player_move(player: Player):
    try:
        x, y = map(lambda num: int(num) if num.isdigit() else False, input("Enter the coordinates: ").split())
    except:
        x, y, = False, False
    while True:
        if not (x and y):
            print("You should enter numbers!")
        elif x > 3 or y > 3:
            print("Coordinates should be from 1 to 3!")
        elif player.board[3 - y][x - 1] in ("X", "O"):
            print("This cell is occupied! Choose another one!")
        else:
            break
        try:
            x, y = map(lambda num: int(num) if num.isdigit() else False, input("Enter the coordinates: ").split())
        except:
            x, y, = False, False
    player.board[3 - y][x - 1] = player.piece


def display_board(board):
    print("---------")
    for row in board:
        print("| ", end="")
        for piece in row:
            print(piece + " " if piece in ["X", "O"] else "  ", end="")
        print("|")
    print("---------")


def check_winner(board):
    if board[0][0] + board[1][1] + board[2][2] in ["XXX", "OOO"] or board[2][0] + board[1][1] + board[0][2] in ["XXX",
                                                                                                                "OOO"]:
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


game_board = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]]

choices = {"easy": easy_move, "user": player_move}
while True:
    choice = input("Input command: ").split()
    if choice[0] == "exit":
        sys.exit()
    elif not len(choice) == 3:
        print("Bad parameters!")
    elif all(param in ("easy", "user") for param in choice[1:]) and choice[0] == "start":
        players = (Player(choices[choice[1]], game_board, "X"), Player(choices[choice[2]], game_board, "O"))
        break

turn = 0
display_board(game_board)
while check_winner(game_board) not in ["X", "O", "Draw"]:
    players[turn].make_move()
    turn = (turn + 1) % 2
    display_board(game_board)
print(check_winner(game_board) + " wins" if check_winner(game_board) in ["X", "O"] else "Draw")
