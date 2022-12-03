'''
Allen has a LOT of money. He has n dollars in the bank. For security reasons, he wants to withdraw it in cash (we will not disclose the reasons here). The denominations for dollar bills are 1, 5, 10, 20, 100. What is the minimum number of bills Allen could receive after withdrawing his entire balance?

Input
The first and only line of input contains a single integer n (1≤n≤109).

Output
Output the minimum number of bills that Allen could receive
'''

n=int(input())
coins = [1, 5, 10, 20, 100]

value = {}
'''
#I iterativno i rekurzija je presporo
def fooREKURZIJA(x):
    if(x<0): return float('inf')
    elif(x==0): return 0
    elif x in value: return value[x]
    else:
        best = float('inf')
        for c in coins:
            best = min(best, foo(x-c)+1)
        value[x]=best
        return best

value[0]=0
for i in range(1, n+1):
    value[i]=float('inf')
    for c in coins:
        if i-c >= 0:
            value[i]=min(value[i], value[i-c]+1)
'''

#GREEDY
rez=0
value[0]=0
if(n<100):
    for i in range(1, n+1): 
        value[i]=float('inf')
        for c in coins:
            if i-c >= 0:
                value[i]=min(value[i], value[i-c]+1)
    rez = value[i]
elif(n % 100 != 0):
    n2 = n % 100
    for i in range(1, n2+1): 
        value[i]=float('inf')
        for c in coins:
            if i-c >= 0:
                value[i]=min(value[i], value[i-c]+1)
    rez=value[n2] + int(n/100)
else:   
    rez=int(n/100)


print(rez)