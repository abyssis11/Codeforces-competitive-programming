'''
This week Arkady wanted to cook some pancakes (to follow ancient traditions) and make a problem about that. But then he remembered that one can't make a problem about stacking pancakes without working at a specific IT company, so he decided to bake the Napoleon cake instead.

To bake a Napoleon cake, one has to bake n dry layers first, and then put them on each other in one stack, adding some cream. Arkady started with an empty plate, and performed the following steps n times:

place a new cake layer on the top of the stack;
after the i-th layer is placed, pour ai units of cream on top of the stack.
When x units of cream are poured on the top of the stack, top x layers of the cake get drenched in the cream. If there are less than x layers, all layers get drenched and the rest of the cream is wasted. If x=0, no layer gets drenched.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤20000). Description of the test cases follows.

The first line of each test case contains a single integer n (1≤n≤2⋅105) — the number of layers in the cake.

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤n) — the amount of cream poured on the cake after adding each layer.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.

Output
For each test case, print a single line with n integers. The i-th of the integers should be equal to 1 if the i-th layer from the bottom gets drenched, and 0 otherwise.
'''

t = int(input())
rez = []

for i in range(t):
    n = int(input())
    test = [int(x) for x in input().split(' ')]
    for i in range(n-2, -1, -1):
        # max(test[i+1]-1,0) usporedjujemo s 0 jer nam ne treba manje od 0
        test[i] = max(test[i], max(test[i+1]-1,0))
    
    rez.append(test)

for re in rez:
    rez2 = []
    for r in re:
        rez2.append(1 if r > 0 else 0)
    
    print(' '.join(str(e) for e in rez2))
