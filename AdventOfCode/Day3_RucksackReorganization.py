with open("AdventOfCode\input\Day3.txt") as file:
    l = [x for x in file.read().split('\n')]

priorites = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def p1():
    acc = 0
    for ruck in l:
        items = int(len(ruck)/2)
        firstC = ruck[:items]
        secondC = ruck[items:]
        same = [x for x in firstC if x in secondC][0]
        acc += priorites.index(same)
    return acc

def p2():
    acc = 0
    groups = []
    for i in range(0, len(l), 3):
        groups.append(l[i:i+3])

    for group in groups:
        same = [x for x in group[0] if x in group[1] and x in group[2]][0]
        acc += priorites.index(same)   
    return acc

print(p1())    
print(p2())