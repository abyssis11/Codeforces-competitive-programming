with open("AdventOfCode\/2022\input\Day5.txt") as file:
    l = [y for y in (x for x in file.read().split('\n'))]

stacks=[]
l2=[]
l1 = [x.replace('[', '').replace(']', '').replace('  ',' ') for x in l[:l.index('')]]
l3 = [x.replace('move', '').replace('from', '').replace('to', '') for x in l[l.index('')+1:]]
for x in l3:
    l2.append(x.split(' '))

l2 = [[i for i in x if i != ''] for x in l2]

stacks=['']*(len(l1[-1]))
l1.pop()
for s in l1:
    for l in s:
        if l != ' ':
            stacks[s.index(l)]+=l
            s=s.replace(l,' ',1)

stacks=[x for x in stacks if x != '']
a=0
for s in l2:
    acc = 0
    a+=1
    r=''
    if int(s[0]) > len(stacks[int(s[1])-1]):
        num=len(stacks[int(s[1])-1])
    else:
        num = int(s[0])
    for i in range(num):
        
        stacks[int(s[2])-1] = stacks[int(s[1])-1][acc] + stacks[int(s[2])-1]
        r+=stacks[int(s[1])-1][acc]
        acc+=1
    stacks[int(s[1])-1]=stacks[int(s[1])-1].replace(r,'',1) #PAZI!!!!!!!!! samo jedanput brisemo

print(''.join([x[0] for x in stacks if len(x)]))
