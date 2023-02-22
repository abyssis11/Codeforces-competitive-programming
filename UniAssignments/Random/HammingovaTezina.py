inp = input()
inp = int(inp, 2)

res=0
while inp:
    res += inp%2
    inp = inp >> 1

print(res)