inp = [int(x) for x in input().split(' ')]

def foo(iter, acc):
    if(iter < 1):
        return acc
    manji = min(inp[iter], inp[iter-1])
    newAcc=acc+manji
    if(newAcc-acc==inp[iter]):
        iter-=1
    else:
        iter-=2
    return foo(iter, newAcc)

print(foo(len(inp)-1, 0))