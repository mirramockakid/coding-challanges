
from os import close
import numpy as np
import pandas as pd
from statistics import mode
import re

test = "3,4,3,1,2"

# initialise list
fish_by_day = [0] * 9
for i in re.split(',', test):
    fish_by_day[int(i)] = fish_by_day[int(i)] + 1

# propergate list
days = 80

for d in range(days):
    print(d)
    
    # fish day 0 - save so can place back to 6
    mem_zero = fish_by_day[0]
    fish_by_day[0] = 0
    
    # fish day 1 - 9 - shift down 1
    for i in range(1,9):
        fish_by_day[i - 1] = fish_by_day[i]
    
    # add day 0 to day 6
    fish_by_day[6] = fish_by_day[6] + mem_zero
    
    # add new fish
    fish_by_day[8] = mem_zero

sum(fish_by_day)


#path = "./day5_input.txt"
#vents_map = open(path,'r')
#for line in vents_map:
