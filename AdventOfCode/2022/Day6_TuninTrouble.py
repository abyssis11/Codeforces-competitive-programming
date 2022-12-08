with open("AdventOfCode\/2022\input\Day6.txt") as file:
    lista = file.read()

def p1_2(distinct):
    acc=''
    for i in range(len(lista)):
        acc=lista[i]
        for j in range(i+1,i+distinct):
            if lista[j] not in acc:
                acc+=lista[j]
            if len(acc)==distinct:
                return j+1

print(p1_2(4))
print(p1_2(14))
    
    