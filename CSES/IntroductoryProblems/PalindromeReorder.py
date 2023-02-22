inp = input()
slova = {}

for i in inp:
    if i not in slova:
        slova[i]=1
    else:
        slova[i]+=1

FrontString = ''
LonelyString = ''
BackString = ''
acc = 0 

for key in slova:
    if slova[key] % 2 == 0:
        num = int(slova[key] / 2)
        FrontString += key * num
        back = key * num
        BackString = back + BackString
    else:
        if acc == 1:
            break
        acc+=1
        num = int(slova[key])
        LonelyString += key * num

string = FrontString + LonelyString + BackString

if len(string) == len(inp):
    print(string)
else:
    print('NO SOLUTION')