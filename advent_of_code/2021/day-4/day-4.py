import numpy as np
import re
import copy

with open('./day4_input.txt') as f:
    read_data = f.read()

read_data = read_data.strip().split('\n')

draws  = read_data[0].split(",")
boards = []
board = []

for i in range(2, len(read_data)):
    if (read_data[i] == ''):
        board = np.array(board)
        boards.append(board)
        board = []
    else:

        l = re.split(' +', read_data[i].strip())
        for e in range(len(l)):
            l[e] = int(l[e])
        board.append(l)

# empty to keep score
marks = copy.deepcopy(boards)
for m in marks:
    m.fill(0)

res = []
found = 0
res_brd = []

for d in range(len(draws)):
    ball = int(draws[d])
    for b in range(len(boards)):
        board = boards[b]
        if (ball in board):
            coord = np.where(ball == board)
            marks[b][coord] = 1
            if (np.sum(marks[b][coord[0]]) == 5):
                umrk_tot = np.sum(board[np.where(0 == marks[b])])
                if (b not in res_brd):
                    res.append(umrk_tot * ball)
                    res_brd.append(b)
            elif (np.sum(marks[b][:,coord[1]]) == 5):
               # get unmarked total
                umrk_tot = np.sum(board[np.where(0 == marks[b])])
                if (b not in res_brd):
                    res.append(umrk_tot * ball)
                    res_brd.append(b)
