'''
You are given two integers x and y. You can perform two types of operations:

Pay a dollars and increase or decrease any of these integers by 1. For example, if x=0 and y=7 there are four possible outcomes after this operation:
x=0, y=6;
x=0, y=8;
x=−1, y=7;
x=1, y=7.
Pay b dollars and increase or decrease both integers by 1. For example, if x=0 and y=7 there are two possible outcomes after this operation:
x=−1, y=6;
x=1, y=8.
Your goal is to make both given integers equal zero simultaneously, i.e. x=y=0. There are no other requirements. In particular, it is possible to move from x=1, y=0 to x=y=0.

Calculate the minimum amount of dollars you have to spend on it.

Input
The first line contains one integer t (1≤t≤100) — the number of testcases.

The first line of each test case contains two integers x and y (0≤x,y≤109).

The second line of each test case contains two integers a and b (1≤a,b≤109).

Output
For each test case print one integer — the minimum amount of dollars you have to spend.
'''
test = int(input())
results=[]
for i in range(test):
    xy = [int(x) for x in input().split()]
    y=xy.pop()
    x=xy.pop()

    ab = [int(x) for x in input().split()]
    b = ab.pop()
    a = ab.pop()

    diff=abs(x-y)
    toEq=diff * a
    lower = min(x, y)
    if (2 * a) < b:
        toZero = lower * 2 * a
    else:
        toZero = lower * b
    
    results.append(toZero+toEq)

for r in results:
    print(r)

