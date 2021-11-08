# coding-challanges

Challange is described [here](https://adventofcode.com/2016/day/8)

import numpy as np
import re
np.set_printoptions(threshold=np.inf)

# initialise a matrix of zeros
mat = np.zeros((6,50), dtype=np.int32)

infile = open("test_input.txt", "r")

for line in infile:
    if line.startswith("rect"):
        ret = rotate_format(line)
        turn_on_pix(ret[0],ret[1], mat)
    elif line.startswith("rotate row"):
        ret = rotate_format(line)
        rotate_row(ret[0], ret[1], mat)
    elif line.startswith("rotate column"):
        ret = rotate_format(line)
        rotate_col(ret[0], ret[1], mat)

# number of lit
np.count_nonzero(mat)
# 116

# print leters
# result = "UPOJFLBCEZ"
i = 0
while i < 49:
    mat[:,i:i+4]
    i = i+5

def rotate_row(row, by, mat):
    mat[int(row),:] = np.roll(mat[int(row),:], int(by))
    return mat

def rotate_col(col, by, mat):
    mat[:,int(col)] = np.roll(mat[:,int(col)], int(by))
    return mat

def rotate_format(line):
    catch =  re.findall("\d+", line)
    return catch

def turn_on_pix(col,row, mat):
    mat[:int(row),:int(col)] = 1
    return mat
