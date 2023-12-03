def partA():
    partA = 0
    s = open("Day 3/input.txt", "r").read().split("\n")
    sa = [list(i) for i in s]
    def d(a):
        e = []
        d = ""
        for x in a:
            if x.isdigit():
                d += x
            else:
                if d:
                    e.extend([d] * len(d))
                    d = ""
                e.append(x)
        if d:
            e.extend([d] * len(d))
        return e

    sa = [d(a) for a in sa]


    def sp(a, b, sa):
        sc = set(['*', '#', '+', '$', '&', '=', '%', '@', '-', '!', '^', '(', ')', '_', '/'])
        for i in range(a-1, a+2):
            for j in range(b-1, b+2):
                if 0 <= i < len(sa) and 0 <= j < len(sa[i]) and (i != a or j != b) and sa[i][j] in sc:
                    return True
        return False

    same = False

    for i in range(len(sa)):
        for j in range(len(sa[i])):
            if not same and sa[i][j].isdigit() and sp(i, j, sa):
                partA += int(sa[i][j])
                same = True
            elif same and sa[i][j].isdigit() and sp(i, j, sa):
                continue
            else:
                same = False

    print(partA)


def partB():
    partB = 0
    s = open("Day 3/input.txt", "r").read().split("\n")
    sa = [list(i) for i in s]

    def d(a):
        e = []
        d = ""
        for x in a:
            if x.isdigit():
                d += x
            else:
                if d:
                    e.extend([d] * len(d))
                    d = ""
                e.append(x)
        if d:
            e.extend([d] * len(d))
        return e

    sa = [d(a) for a in sa]

    for i in range(len(sa)):
        for j in range(len(sa[i])):
            if sa[i][j] == '*':
                n = []
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if 0 <= x < len(sa) and 0 <= y < len(sa[x]) and (x != i or y != j) and sa[x][y].isdigit():
                            n.append(int(sa[x][y]))

                if len(set(n)) == 2:
                    print(n)
                    result = n[0] * n[-1]
                    partB += result

    print(partB)
partB()