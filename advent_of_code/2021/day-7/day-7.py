from collections import Counter
from statistics import median

input = "./day7_input.txt"
input_pos = open(input, "r").read().strip()

#input_pos = "16,1,2,0,4,2,7,1,2,14"

pos = list(map(int, input_pos.split(",")))
pos_dic = Counter(pos)

# part 1
centre = median(pos)
print("Median is: ", centre)
cnt = 0
for p in pos_dic:
    cnt += abs((int(p) - centre) * pos_dic[p])

print("Part 1: ", cnt)

# part 2 - search for min fule between 400 - 500
# which seems reasonable given the median
min_fule = 1e8
for c in range(300,500):
    cnt = 0
    for p in pos_dic:
        n = abs((int(p) - c))
        cnt += ((n * (n + 1)) / 2) * pos_dic[p]
    if (cnt < min_fule):
        min_fule = cnt

print("Part 2: ", min_fule)