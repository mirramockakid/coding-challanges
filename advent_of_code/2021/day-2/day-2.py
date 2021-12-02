from _typeshed import SupportsAnext
from os import close
import re

start_coord = 0
depth = 0
hzl = 0
aim = 0

## part 1
path = "./day2_input.txt"
sea_map = open(path,'r')
for line in sea_map:
    #pattern = "r(\d+)\s+(\w+)\s+(\d+)"
    exp = re.match(r"(\w+)\s+(\d+)", line)
    
    if (exp.group(1) == "forward"):
        hzl += int(exp.group(2))
        depth += int(exp.group(2)) * aim
    elif (exp.group(1) == "up"):
        #depth -= int(exp.group(2))
        aim -= int(exp.group(2))
    elif (exp.group(1) == "down"):
        #depth += int(exp.group(2))
        aim += int(exp.group(2))

print(depth)
print(hzl)
print(depth * hzl)

sea_map.close()