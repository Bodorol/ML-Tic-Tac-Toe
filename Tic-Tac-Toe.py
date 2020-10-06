import random
import sys
import os

win_positions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8))


class Player:

    def __init__(self, move, board, piece):
        self.move = move
        self.board = board
        self.piece = piece

    def make_move(self):
        self.move(self)


def easy_move(player):
    print('Making move level "easy"')
    x, y = random.randint(0, 2), random.randint(0, 2)
    while player.board[x + 3 * (2 - y)] in ("X", "O"):
        x, y = random.randint(0, 2), random.randint(0, 2)
    player.board[x + 3 * (2 - y)] = player.piece
    sys.stdout = sys.__stdout__


def medium_move(player):
    print('Making move level "medium"')
    pieces = ("X", "O")
    index = pieces.index(player.piece)
    for _ in range(2):
        for set in win_positions:
            pos = (player.board[set[0]], player.board[set[1]], player.board[set[2]])
            if pos.count(pieces[index]) == 2 and "_" in pos:
                player.board[set[pos.index("_")]] = player.piece
                return
        index = (index + 1) % 2
    sys.stdout = open(os.devnull, 'w')
    easy_move(player)


def hard_move(player):
    print('Making move level "hard"')

    def mini_max(real_player, board=player.board.copy(), piece=player.piece):
        avail_spots = [index for (index, piece) in enumerate(board) if piece == "_"]
        if check_winner(board) == real_player.piece:
            return 10
        elif check_winner(board) == "Draw":
            return 0
        elif check_winner(board) is not None:
            return -10
        if player.piece == piece:
            best = -1000
            for i in avail_spots:
                board[i] = piece
                best = max(best, mini_max(real_player, board, ("X", "O")[(("X", "O").index(piece) + 1) % 2]))
                board[i] = "_"
            return best
        else:
            best = 1000
            for i in avail_spots:
                board[i] = piece
                best = min(best, mini_max(real_player, board, ("X", "O")[(("X", "O").index(piece) + 1) % 2]))
                board[i] = "_"
            return best

    avail_spots = [index for (index, piece) in enumerate(player.board) if piece == "_"]
    if len(avail_spots) == 9:
        sys.stdout = open(os.devnull, 'w')
        easy_move(player)
        return
    best_spot = -1
    best_val = -1000
    for i in avail_spots:
        player.board[i] = player.piece
        move_val = mini_max(player, player.board, ("X", "O")[(("X", "O").index(player.piece) + 1) % 2])
        if move_val > best_val:
            best_val = move_val
            best_spot = i
        player.board[i] = "_"
    player.board[best_spot] = player.piece


def player_move(player):
    try:
        x, y = map(lambda num: int(num) if num.isdigit() else False, input("Enter the coordinates: ").split())
    except:
        x, y, = False, False
    while True:
        if not (x and y):
            print("You should enter numbers!")
        elif x > 3 or y > 3:
            print("Coordinates should be from 1 to 3!")
        elif player.board[(x - 1) + 3 * (y - 1)] in ("X", "O"):
            print("This cell is occupied! Choose another one!")
        else:
            break
        try:
            x, y = map(lambda num: int(num) if num.isdigit() else False, input("Enter the coordinates: ").split())
        except:
            x, y, = False, False
    player.board[(x - 1) + 3 * (y - 1)] = player.piece


def display_board(board):
    print("---------")
    for i in range(3):
        print("|", " ".join([x if x in ("X", "O") else " " for x in board[i * 3:(i + 1) * 3]]), "|")
    print("---------")


def check_winner(board):
    unfinished = False
    for set in win_positions:
        pos = (board[set[0]], board[set[1]], board[set[2]])
        if pos in (("X", "X", "X"), ("O", "O", "O")):
            return pos[0]
        elif "_" in pos:
            unfinished = True
    if unfinished:
        return
    else:
        return "Draw"


game_board = ["_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

choices = {"easy": easy_move, "medium": medium_move, "hard": hard_move, "user": player_move}
while True:
    choice = input("Input command: ").split()
    if choice[0] == "exit":
        sys.exit()
    elif all(param in ("easy", "medium", "hard", "user") for param in choice[1:]) and choice[0] == "start" and len(
            choice) == 3:
        players = (Player(choices[choice[1]], game_board, "X"), Player(choices[choice[2]], game_board, "O"))
        break
    else:
        print("Bad parameters!")

turn = 0
display_board(game_board)
while check_winner(game_board) not in ("X", "O", "Draw"):
    players[turn].make_move()
    turn = (turn + 1) % 2
    display_board(game_board)
print(check_winner(game_board) + " wins" if check_winner(game_board) in ("X", "O") else "Draw")
