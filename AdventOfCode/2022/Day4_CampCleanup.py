with open("AdventOfCode\/2022\input\Day4.txt") as file:
    l = [x for x in file.read().split('\n')]

def p1():
    acc=0
    for pair in l:
        sp = pair.split(',')
        pair1 = [int(x) for x in sp[0].split('-')]
        pair2 = [int(x) for x in sp[1].split('-')]
        if(pair1[0] <= pair2[0] and pair1[1] >= pair2[1]) or (pair2[0] <= pair1[0] and pair2[1] >= pair1[1]):
            acc+=1
    return acc

def p2():
    acc=0
    for pair in l:
        sp = pair.split(',')
        pair1 = [int(x) for x in sp[0].split('-')]
        pair2 = [int(x) for x in sp[1].split('-')]
        if min(pair1[1], pair2[1]) - max(pair1[0], pair2[0]) >=0:
            acc+=1
    return acc

print(p1())
print(p2())

    
