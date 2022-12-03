#Generous Kafe
b=int(input().split()[1])
c=input()
#set(c) napravi polje sa unikatnim elementima od c 
# i onda te elemente prebrojimo u c
# uzimamo broj ponavljanja slova koji se najvise ponavlja
# ako je veci od broja prijatelja onda vraca true
# truje vraca drugi element u listi prije a false vraca prvi element
print( ["YES", "NO"][ max(c.count(i) for i in set(c)) > b ] )