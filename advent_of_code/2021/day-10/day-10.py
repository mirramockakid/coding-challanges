import re
from collections import Counter
import statistics

input = "./day10_input.txt"

op = ['(','[','{','<']
cl = [')',']','}','>']
corr = Counter({')':0, ']':0, '}':0, '>':0})
to_complete = []

with open(input, "r") as infile:
    for l in infile:
        opmem = []
        incomp = True
        l = l.strip()
        for i, v in enumerate(l):
            if v in op:
                opmem.append(v)
            else:
                x = opmem.pop()
                if cl[op.index(x)] != v:
                    corr.update(v)
                    incomp = False
                    break
        if (incomp == True):
            to_complete.append(compscore(opmem))

(corr['}'] * 1197) + (corr[')'] * 3) + (corr['>'] * 25137) + (corr[']'] * 57)
statistics.median(to_complete)


def compscore(x):
    score = 0
    for i in x[::-1]:
        score = score * 5
        if (i == '['):
            score += 2
        elif (i == '('):
            score += 1
        elif (i == '<'):
            score += 4
        elif (i == '{'):
            score += 3
        
    return(score)