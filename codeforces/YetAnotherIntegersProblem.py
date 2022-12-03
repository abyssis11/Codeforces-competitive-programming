'''
You are given two integers a and b.

In one move, you can choose some integer k from 1 to 10 and add it to a or subtract it from a. In other words, you choose an integer k∈[1;10] and perform a:=a+k or a:=a−k. You may use different values of k in different moves.

Your task is to find the minimum number of moves required to obtain b from a.

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤2⋅104) — the number of test cases. Then t test cases follow.

The only line of the test case contains two integers a and b (1≤a,b≤109).

Output
For each test case, print the answer: the minimum number of moves required to obtain b from a.
'''
k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = int(input())
tests = []
for i in range(t):
    c = [int(x) for x in input().split(' ')]
    tests.append(c)

for test in tests:
    #sum = 0
    s = abs(test[1]-test[0])
    if(s % 10 == 0):
        print(int(s/10))
    else:
        # ako nije djeljivo s 10 
        # onda je sigurno umanjeno za jedan bilokoji broj iz k djeljivo s 10 
        print(int(s/10)+1)
    
'''
# PRE DUGO RADI
k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#k = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
t = int(input())
tests = []
for i in range(t):
    c = [int(x) for x in input().split(' ')]
    tests.append(c)
value = {}
for test in tests:
    value[0]=0
    s = abs(test[1]-test[0])
    for x in range (1, s+1):
        value[x]=float('inf')
        for c in k:
            if x-c >= 0:
                value[x] = min(value[x], value[x-c]+1)
    print(value[s])
'''

'''
# NE RADI - ZAPNE U REKURZIJI
t = int(input())
tests = []
k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#k = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
value = {}
#value[1]=2
#value[2]=3
#print(value[2])

for i in range(t):
    c = [int(x) for x in input().split(' ')]
    tests.append(c)

def foo3(x):
    for i in range(1, x):
        value[i] = float('inf')
        for ks in k:
            if(i-ks >= 0):
                value[i] = min(value[i], value[i-ks]+1)

def foo2(x):
    if (x<0): return float('inf')
    elif (x==0): return 0
    elif x in value: return value[x]
    elif x % 10 == 0:
        best = int(x/10)
        value[x] = best
        return best
    elif(x % 9 == 0):
        best = int(x/9)
        value[x] = best
        return best
    else:
        best = float('inf')
        for ks in k:
            best = min(best, foo2(x-ks)+1)
        value[x]=best
        return best


def foo(s, ks, acc):
    if(s==0):
        return acc
    elif(s-max(ks)>=0):
        acc+=1
        s-=max(ks)
    else:
        ks.pop()
    return foo(s, ks, acc)
        
for test in tests:
    s = abs(test[1]-test[0])
    #ks = k
    #foo3(s)
    print(foo2(s))

'''