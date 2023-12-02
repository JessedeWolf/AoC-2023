import re
partA, partB, gameNr = 0, 0, 0
s = open("Day 2/input.txt", "r").read().split("\n")
red = re.compile(r'(\d+) red')
green = re.compile(r'(\d+) green')
blue = re.compile(r'(\d+) blue')
for x in s:
    gameNr+=1
    g = max(map(int, green.findall(x)))
    b = max(map(int, blue.findall(x)))
    r = max(map(int, red.findall(x)))
    partB += r * g * b
    if g > 13 or b > 14 or r > 12:
        continue
    else:
        partA += gameNr
print(f"A: {partA}     B: {partB}")