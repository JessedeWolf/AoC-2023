import re
def partA():
    allNr = []
    ownNr = []
    cardNr = []
    matches = []
    y = 0
    total = 0
    s = open("Day 4/input.txt", "r").read().split("\n")
    for x in s:
        # print(x)
        allNr = re.sub(r'^.*?:', '', x)
        allNr = allNr.split("|")
        cardNr = allNr[0].split(" ")
        ownNr = allNr[1].split(" ")

        while '' in cardNr:
            cardNr.remove('')
        while '' in ownNr:
            ownNr.remove('')
        matches = list(set(cardNr).intersection(ownNr))

        if len(matches) == 1:
            total += 1
        elif len(matches) == 0:
            total += 0
        else:
            y = len(matches) - 1
            total += 2 ** y
    print(total)

def partB():
    allNr, ownNr, cardNr, matches, lmaotest, individual_matches = [], [], [], [], [], []
    rounds = 0
    card_count = 0

    s = open("Day 4/input.txt", "r").read().split("\n")
    for x in s:
        rounds += 1
        allNr = re.sub(r'^.*?:', '', x)
        allNr = allNr.split("|")
        cardNr = allNr[0].split(" ")
        ownNr = allNr[1].split(" ")

        while '' in cardNr:
            cardNr.remove('')
        while '' in ownNr:
            ownNr.remove('')
        matches = list(set(cardNr).intersection(ownNr))

        if matches:
            if len(lmaotest) != 0:
                for x in range(len(lmaotest)):
                    individual_matches.append(len(matches))  
                    lmaotest.extend(individual_matches[-1:])
            else:
                individual_matches.append(len(matches))  

            lmaotest.extend(individual_matches[-1:])

        while 0 in lmaotest:
            lmaotest.remove(0)
        print(f"{rounds} {len(lmaotest)}")

        card_count += len(lmaotest)

        lmaotest = [x - 1 for x in lmaotest if x > 0]

    print(card_count + rounds)

partB()