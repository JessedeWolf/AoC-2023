time = ['46', '68', '98', '66']
distance = ['358', '1054', '1807', '1080']

rtime = ''.join(time)
rdistance = ''.join(distance)


def partA():
    cntr = 0
    total = 1
    empty = []
    empty2 = []
    for i in time:
        for x in range(int(i)+1):
            if (int(i) - x) * x > int(distance[cntr]):
                empty.append(x)
        empty2.append(len(empty))
        empty = []
        cntr += 1

    for x in empty2:
        total *= int(x)
    print(total)

def partB():
    empty3 = []
    for y in range(int(rtime)):
        if y * (int(rtime) - y) > int(rdistance):
            empty3.append(y)
    print(len(empty3))

partA()
partB()