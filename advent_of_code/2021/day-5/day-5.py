from _typeshed import SupportsAnext
from os import close
import numpy as np
import pandas as pd
from statistics import mode
import re

start_list = []
end_list   = []
row = [0,0]
col = [0,0]
row_max = 0
col_max = 0
path = "./testinput.txt"
vents_map = open(path,'r')
for line in vents_map:
    coord = re.split(' -> ', line.strip())
    start = re.split(',', coord[0])
    end   = re.split(',', coord[1])
    start_list.append(start)
    end_list.append(end)
    
    if (row_max < int(max(start[1], end[1]))):
        row_max = int(max(start[1], end[1]))
    
    if (col_max < int(max(start[0], end[0]))):
        col_max = int(max(start[0], end[0]))

# create empty map
mat = np.zeros((int(row_max) + 1, int(col_max) + 1), dtype=np.int32)

for i in range(len(start_list)):
    
    if (start_list[i][0] != end_list[i][0] and start_list[i][1] != end_list[i][1]):
        print("Diag")
        print(start_list[i], end_list[i])
        
        row[0] = int(start_list[i][1])
        row[1] = int(end_list[i][1])
        col[0] = int(start_list[i][0])
        col[1] = int(end_list[i][0])
        
        row_range = range(row[0], row[1])
        if (row[0] > row[1]):
            reversed(row_range)
        
        col_range = range(col[0], col[1])
        if (col[0] > col[1]):
            reversed(col_range)
        
        element_cnt = 0
        while (element_cnt <= len(col_range) and element_cnt <= len(row_range)):
            print(mat)
            mat[row_range[element_cnt]:row_range[element_cnt]+1, row_range[element_cnt]:row_range[element_cnt]+1] = mat[row_range[element_cnt]:row_range[element_cnt]+1, row_range[element_cnt]:row_range[element_cnt]+1] + 1
            element_cnt += 1
            print(mat)
    else:
        print("Line")
        
        row[0] = int(start_list[i][1])
        row[1] = int(end_list[i][1])
        col[0] = int(start_list[i][0])
        col[1] = int(end_list[i][0])
        
        if (row[0] > row[1]):
            row.insert(0, row.pop())
        
        if (col[0] > col[1]):
            col.insert(0, col.pop())
        
        mat[row[0]:row[1]+1, col[0]:col[1]+1] = mat[row[0]:row[1]+1, col[0]:col[1]+1] + 1

np.sum(mat > 1)



