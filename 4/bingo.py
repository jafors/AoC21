


def check(board):
    rowwise = colwise = False
    for row in board:
        rowwise |= all(row.values())
    for i in range(0, len(board[0])):
        colwise |= all([list(r.values())[i] for r in board])
    return(colwise | rowwise)

def mark(boards, number):
    winning_boards = []
    new_boards = []
    for board in boards:
        for row in board:
            if number in row:
                row[number] = True
                break
        bingo = check(board)
        if bingo:
            winning_boards.append(board)
            continue
        new_boards.append(board)
    return((new_boards, winning_boards))

input_data = open("bingo_input.txt")
numbers = next(input_data).rstrip().split(",")
board = []
boards = []
for line in input_data:
    if not line.rstrip():
        if board != []:
            boards.append(board)
        board = []
    else:
        board.append({int(k):False for k in line.rstrip().split()})

winning = []
for number in numbers:
    boards, winning_boards = mark(boards, int(number))
    for wb in winning_boards:
        score = sum([k for r in wb for k,v in r.items() if not v])
        winning.append((wb, score, number, score * int(number)))
    winning_boards = []
print(winning[0][3])
print(winning[-1][3])
