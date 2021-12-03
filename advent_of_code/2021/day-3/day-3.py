from _typeshed import SupportsAnext
from os import close
import numpy as np
import pandas as pd
from statistics import mode
import re

# gamma = 000110001010
# 394

# epsilon = 111001110101
# 3701
start = 0
mat = []
path = "./day3_input.txt"
codes = open(path,'r')
for line in codes:
    l = list(line.strip())
    mat.append(l)

array = np.array(mat).astype(int)

# part #1
mode_bit = list(np.rint((sum(array)/len(array))).astype(int))
for i in range(len(mode_bit)):
    mode_bit[i] = str(mode_bit[i])

print(''.join(mode_bit), sep = "")

for i in range(np.shape(array)[1]):
    print(np.shape(array))
    vec = array[:,i]
    if (sum(vec)/len(vec) < 0.5):
        start = 1
    else:
        start = 0
    
    array = array[(vec == start)]
    print(array)

# oxygen gen
# [[0 0 1 1 0 0 0 1 0 1 0 1]] = 789

# CO2
# [[1 1 1 0 0 0 0 0 0 0 1 0]] = 3586

789*3586