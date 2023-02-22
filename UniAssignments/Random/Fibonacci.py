inp = int(input())
# fibs = [0] * (inp+1)
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if fibs[n]:
#         return fibs[n]
#     currentFib = fib(n-1) + fib(n-2)
#     fibs[n] = currentFib
#     return currentFib

# def fib(n):
#     mem = [0, 1]
#     for i in range(2, n+1):
#         mem.append(mem[i-1]+mem[i-2])
#     return mem

def fib(n):
    a = 0
    b = 1
    if n == 0: return a
    if n == 1: return b
    for _ in range(2, n+1):
        c = a+b
        a=b
        b=c
    return b
        

print(fib(inp) % (pow(10,9) +7))