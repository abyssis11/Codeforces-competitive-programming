inp = int(input())
coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins = coins[::-1]
UsedCoins = []
def fun(inp):
    if inp == 0:
        return
    else:
        for c in coins:
            if inp - c >=0:
                inp = inp - c
                UsedCoins.append(c)
                break
    fun(inp)

fun(inp)

print(' '.join(str(x) for x in UsedCoins))

