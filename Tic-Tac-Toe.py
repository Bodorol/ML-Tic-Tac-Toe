import re

# XOXO_OXO_
startup = list(input())
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(startup[j + 3 * i])
    board.append(row)
char = "X" if len([x for x in re.finditer("X", "".join(startup))]) == len([x for x in re.finditer("O", "".join(startup))]) else "O"
print(board)
x, y = map(lambda num: int(num) if num.isdigit() else False, input().split())
if not (x and y):
    print("You should enter numbers!")
elif x > 3 or y > 3:
    print("Coordinates should be from 1 to 3!")
elif board[x - 1][y - 1] in ("X", "O"):
    print("This cell is occupied! Choose another one!")
else:
    board[x - 1][y - 1] = char
print(board)