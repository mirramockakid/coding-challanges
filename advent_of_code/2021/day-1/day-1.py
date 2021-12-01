#!/bin/python

from _typeshed import SupportsAnext
from os import close

## part 1
inc = 0
path = "./day1_input.txt"
tree_map = open(path,'r')
for line in tree_map:
    value = int(line.strip())
    if (value > mem):
        inc += 1
    mem = value

tree_map.close()
print(inc)

## part 2
set_of_three = []
inc = 0
first = True
mem = 1000000000
path = "./day1_input.txt"
tree_map = open(path,'r')
for line in tree_map:
    value = int(line.strip())
    set_of_three.append(value)
    if (len(set_of_three) == 3):
        if (sum(set_of_three) > mem):
            inc += 1
        mem = sum(set_of_three)
        set_of_three.pop(0)


print(inc)