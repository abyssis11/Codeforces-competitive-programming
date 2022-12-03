with open("AdventOfCode\input\Day2.txt") as file:
    l = [x for x in file.read().split('\n')]


'''
A - rock
B - paper
C - scissors

X - rock (1)
Y - paper (2)
Z - scissors (3)

WIN = 6
DRAW = 3
LOST = 0
'''
score = {
    'A X' : 4,
    'A Y' : 8,
    'A Z' : 3,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 7,
    'C Y' : 2,
    'C Z' : 6
}

'''
X - LOSE
Y - DRAW
Z - WIN
'''
plays = {
    'A X' : 3,
    'A Y' : 4,
    'A Z' : 8,
    'B X' : 1,
    'B Y' : 5,
    'B Z' : 9,
    'C X' : 2,
    'C Y' : 6,
    'C Z' : 7
}

def p1_2(list):
    rez = 0
    for pair in l:
        rez += list[pair]
    return rez

print(p1_2(score))
print(p1_2(plays))