from multiprocessing import Process
n = int(input())
tshrts = []

def takeSecond(elem):
    return elem[1]

for i in range(n):
    r= [int(x) for x in input().split(" ")]
    tshrts.append(r)

nCostumers = int(input())
costumers= [int(x) for x in input().split(" ")]

#tshrts.sort(key=takeSecond)

tshrts = sorted(tshrts, key = lambda x: (x[1], -x[0]), reverse=True)
#print(tshrts)
nShrts = []
nShrtsCOPY = []
nShrtsCOPY2 = []
nShrtsCOPY3 = []
nShrtsCOPY4 = []
nShrtsCOPY5 = []
nShrtsCOPY6 = []
nShrtsCOPY7 = []
first_half=costumers[:n]
sec_half=costumers[n:]

first_half1 = first_half[:n]
sec_half1 = first_half[n:]

first_half2 = sec_half[:n]
sec_half2 = sec_half[n:]
####
first_half3 = first_half1[:n]
sec_half3 = first_half1[n:]

first_half4 = sec_half1[:n]
sec_half4 = sec_half1[n:]

first_half6 = first_half2[:n]
sec_half6 = first_half2[n:]

first_half7 = sec_half2[:n]
sec_half7 = sec_half2[n:]
###

for c in first_half3:
    acc = 0
    for t in tshrts:
        if c-t[0] >=0:
            acc+=1
            c-=t[0]
        if(c==0):
            break
    nShrts.append(acc)

for c in sec_half3:
    acc = 0
    for t in tshrts:
        if c-t[0] >=0:
            acc+=1
            c-=t[0]
        if(c==0):
            break
    nShrtsCOPY.append(acc)

for c in first_half4:
    acc = 0
    for t in tshrts:
        if c-t[0] >=0:
            acc+=1
            c-=t[0]
        if(c==0):
            break
    nShrtsCOPY2.append(acc)

for c in sec_half4:
    acc = 0
    for t in tshrts:
        if c-t[0] >=0:
            acc+=1
            c-=t[0]
        if(c==0):
            break
    nShrtsCOPY3.append(acc)

for c in first_half6:
    acc = 0
    for t in tshrts:
        if c-t[0] >=0:
            acc+=1
            c-=t[0]
        if(c==0):
            break
    nShrtsCOPY4.append(acc)

for c in sec_half6:
    acc = 0
    for t in tshrts:
        if c-t[0] >=0:
            acc+=1
            c-=t[0]
        if(c==0):
            break
    nShrtsCOPY5.append(acc)

for c in first_half7:
    acc = 0
    for t in tshrts:
        if c-t[0] >=0:
            acc+=1
            c-=t[0]
        if(c==0):
            break
    nShrtsCOPY6.append(acc)

for c in sec_half7:
    acc = 0
    for t in tshrts:
        if c-t[0] >=0:
            acc+=1
            c-=t[0]
        if(c==0):
            break
    nShrtsCOPY7.append(acc)

joinedlist = nShrts + nShrtsCOPY +nShrtsCOPY2 +nShrtsCOPY3 +nShrtsCOPY4 +nShrtsCOPY5+ nShrtsCOPY6+nShrtsCOPY7

print(' '.join(str(e) for e in joinedlist))

