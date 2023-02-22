inp = int(input())
act = []

for _ in range (inp):
    act.append([int(x) for x in input().split()])

act.sort(key = lambda x: x[1])
upisani = [act[0]]

for i in act:
    start, end = i
    if start >= upisani[-1][1]:
        upisani.append(i)

print(upisani)