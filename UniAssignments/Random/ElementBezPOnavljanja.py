l = [int(x) for x in input().split(" ")]
res = 0
for b in l:
    res ^= b
print(res)
