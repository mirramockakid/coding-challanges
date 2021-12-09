import numpy as np
import re

input = "./test.txt"
input_file = open(input, "r").read()

# read file to numpy array
mat = []
for i in re.split("\n", input_file.strip()):
    mat.append(list(i))
mat = np.array(mat, dtype="int")

risk = 0
for r in range(np.shape(mat)[0]):
    for c in range(np.shape(mat)[1]):
        current = int(mat[r,c])
        # above
        if r != 0:
            above = current < mat[r-1,c]
        else:
            above = True
        # below
        if r != np.shape(mat)[0] - 1:
            below = current < mat[r+1,c]
        else:
            below = True
        # right
        if c != np.shape(mat)[1] - 1:
            right = current < mat[r,c+1]
        else:
            right = True
        # left
        if c != 0:
            left = current < mat[r,c-1]
        else:
            left = True
        if (all([above,below,left,right])):
            print(r,c, "-->", current)
            risk += (current+1)

print(risk)

low = (4,1)
basin = []

def test(r,c,mat):
    
    visited.append([r,c])
    # check below
    if (check_below(r,c,mat) and [r + 1, c] not in visited):
        test(r + 1, c, mat)
    if (check_above(r,c,mat) and [r - 1, c] not in visited):
        test(r - 1, c, mat)
    if (check_left(r,c,mat) and [r, c - 1] not in visited):
        test(r, c - 1, mat)
    if (check_right(r,c,mat) and [r, c + 1] not in visited):
        test(r, c + 1, mat)

def check_below(r,c,mat):
    if (r != np.shape(mat)[0] - 1):
        if (mat[r + 1, c] != 9):
#            basin.append([r + 1, c])
            return(True)
        else:
            return(False)
    else:
        return(False)

def check_above(r,c,mat):
    if r != 0:
        if (mat[r - 1, c] != 9):
#            basin.append([r - 1,c])
            return(True)
        else:
            return(False)
    else: 
        return(False)

def check_right(r,c,mat):
    if c != np.shape(mat)[1] - 1:
        if (mat[r,c+1] != 9):
#            basin.append([r,c+1])
            return(True)
        else:
            return(False)
    else:
        return(False)

def check_left(r,c,mat):
    if c != 0:
        if (mat[r,c-1] != 9):
#            basin.append([r,c-1])
            return(True)
        else:
            return(False)
    else:
        return(False)

test(0,9,mat)