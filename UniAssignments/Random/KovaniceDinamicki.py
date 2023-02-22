iznos = int(input().split(' ')[1])
kovanice = [int(x) for x in input().split()]
PotrebneKovanice = [float('inf')] * (iznos+1)

# rekurzivno -> RecursionError: maximum recursion depth exceeded in comparison
# def fun(iznos):
#     if iznos < 0: return float('inf')
#     if iznos == 0: return 0
#     if PotrebneKovanice[iznos]: return PotrebneKovanice[iznos]
#     else:
#         best = float('inf') 
#         for k in kovanice:
#             best = min(best, fun(iznos-k)+1)

#         PotrebneKovanice[iznos] = best
#         return best
#fun(iznos)

# iterativno -> time limit
PotrebneKovanice[0] = 0
for i in range (1, iznos+1):
    for k in kovanice:
        if i - k >= 0:
            PotrebneKovanice[i] = min(PotrebneKovanice[i], PotrebneKovanice[i-k]+1)

if PotrebneKovanice[iznos] == float('inf'):
    print(-1)
else:
    print(PotrebneKovanice[iznos])



