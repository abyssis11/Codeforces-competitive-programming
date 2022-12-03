'''
It seems like the year of 2013 came only yesterday. Do you know a curious fact? The year of 2013 is the first year after the old 1987 with only distinct digits.

Now you are suggested to solve the following problem: given a year number, find the minimum year number which is strictly larger than the given one and has only distinct digits.

Input
The single line contains integer y (1000 ≤ y ≤ 9000) — the year number.

Output
Print a single integer — the minimum year number that is strictly larger than y and all it's digits are distinct. It is guaranteed that the answer exists.
'''

y = int(input())
inf = 10000
zaprint = ''
for i in range(y+1, inf):
    broj = []
    year = str(i)
    #print(year)
    for c in year:
        provjera = 1
        for b in broj:
            if len(broj) == 0:
                broj.append(c)
            #print(b)
            if( c == b):
                #print(c)
                provjera = 0
                break
        if(provjera==1):
            broj.append(c)
        else:
            break
    if(len(broj)==4):
        for b in broj:
            zaprint += b
        break

print(zaprint)