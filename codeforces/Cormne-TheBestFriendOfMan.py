k = [int(x) for x in input().split(' ')][1]
walks=[int(x) for x in input().split(' ')]
n = len(walks)
acc=0
for i in range(1,n):
    w = walks[i-1] + walks[i]
    if(w < k):
        additional = k-w
        walks[i] += additional
        acc+=additional

print(acc)
print(' '.join(str(x) for x in walks))