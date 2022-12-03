'''
One day Kefa found n baloons. For convenience, we denote color of i-th baloon as si — lowercase letter of the Latin alphabet. Also Kefa has k friends. Friend will be upset, If he get two baloons of the same color. Kefa want to give out all baloons to his friends. Help Kefa to find out, can he give out all his baloons, such that no one of his friens will be upset — print «YES», if he can, and «NO», otherwise. Note, that Kefa's friend will not upset, if he doesn't get baloons at all.

Input
The first line contains two integers n and k (1 ≤ n, k ≤ 100) — the number of baloons and friends.

Next line contains string s — colors of baloons.

Output
Answer to the task — «YES» or «NO» in a single line.

You can choose the case (lower or upper) for each letter arbitrary.
'''
inp = [int(x) for x in input().split(' ')]
colors=input()
k=inp.pop()
n=inp.pop()
color={}
copyDict={}

for c in colors:
    if c in color:
        color[c]+=1
    else:
        color[c]=1

#kopiramo dictionary
copyDict = dict(color)
for key, value in color.items():
        color[key]-=k

for key, value in color.items():
    if(value<=0):
        del copyDict[key]


if(len(copyDict)==0):
    print('YES')
else:
    print('NO')