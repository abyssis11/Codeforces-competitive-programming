acc = []
acc2 = []
#added 2 blank lines at the end of .txt file
with open("AdventOfCode\input\Day1.txt") as file:
    for line in file:
        l=line.rstrip()
        if l != '':
            acc2.append(l)
        else:
            acc.append(sum(int(x) for x in acc2))
            acc2 = []

def p1():
    return max(acc)

def p2(l, a):
    if len(a) == 3:
        return sum(a)
    else:
        a.append(max(l))
        l.remove(max(l))
        return p2(l, a)

print(p1())
print(p2(acc, []))
