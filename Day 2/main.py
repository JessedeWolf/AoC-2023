import re
partA, partB, gameNr = 0, 0, 0
s = open("Day 2/input.txt", "r").read().split("\n")
for x in s:
    gameNr+=1
    g = max(map(int, re.compile(r'(\d+) green').findall(x)))
    b = max(map(int, re.compile(r'(\d+) blue').findall(x)))
    r = max(map(int, re.compile(r'(\d+) red').findall(x)))
    partB += r * g * b
    if g > 13 or b > 14 or r > 12:
        continue
    else:
        partA += gameNr
print(f"A: {partA}     B: {partB}")