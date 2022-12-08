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

def p1():
    stack1=[x for x in stacks if x != '']
    for s in l2:
        acc = 0
        r=''
        num = int(s[0])
        for i in range(num):  
            stack1[int(s[2])-1] = stack1[int(s[1])-1][acc] + stack1[int(s[2])-1]
            r+=stack1[int(s[1])-1][acc]
            acc+=1
        stack1[int(s[1])-1]=stack1[int(s[1])-1].replace(r,'',1) #PAZI!!!!!!!!! samo jedanput brisemo

    print(''.join([x[0] for x in stack1 if len(x)]))

def p2():
    stack1=[x for x in stacks if x != '']
    for s in l2:
        r=''
        num = int(s[0])-1
        while(num>-1): 
            stack1[int(s[2])-1] = stack1[int(s[1])-1][num] + stack1[int(s[2])-1]
            r+=stack1[int(s[1])-1][num]
            num-=1
        stack1[int(s[1])-1]=stack1[int(s[1])-1].replace(r[::-1],'',1) 

    print(''.join([x[0] for x in stack1 if len(x)]))

p1()
p2()