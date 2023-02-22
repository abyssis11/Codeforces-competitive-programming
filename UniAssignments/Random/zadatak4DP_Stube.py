cijena = [int(x) for x in input().split(' ')]

def fun(i, bv):
    if i == len(cijena):
        return sum(bv)
    if i+2 > len(cijena)-1:
        return sum(bv)
    else:
        bv.append(min(cijena[i+1], cijena[i+2]))
        if cijena[i+1] < cijena[i+2]:
            return fun(i+1, bv)
        else: return fun(i+2, bv)

print(min(fun(0, []) + cijena[0], fun(1, []) + cijena[1]))