import numpy as np
import re

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
        print(board)

# empty to keep score
marks = boards
for m in marks:
    m.fill(0)

for d in range(len(draws)):
    for b in range(len(boards)):
        if (int(d) in b): ##
            np.where(b == int(d)) ##





for i in draws:
    print(i)
