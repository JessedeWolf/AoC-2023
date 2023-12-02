import re

def partA():
    s = open("Day 1/input.txt", "r").read().split("\n")
    pattern = re.compile(r'[a-zA-Z]')
    newList = [pattern.sub('', i) for i in s]
    while '' in newList:
        newList.remove('')
    x = 0
    for i in newList:
        c = i[0]
        d = i[-1]
        e = c + d
        x+=int(e)
    print(x)

def partB():
    m = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }
    with open("Day 1/input.txt", "r") as f:
        s = f.read().strip().split("\n")
    r = 0
    for x in s:
        a = None
        b = None
        s = ""
        for y in x:
            c = None
            if y.isdigit():
                c = y
            else:
                s += y
                for k,v in m.items():
                    if s.endswith(k):
                        c = str(v)
            if c is not None:
                b = c
                if a is None:
                    a = c

        r += int(a + b)
    print(r)

partA()
partB()