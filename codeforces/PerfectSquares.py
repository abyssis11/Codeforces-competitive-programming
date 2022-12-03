'''
Given an array a1, a2, ..., an of n integers, find the largest number in the array that is not a perfect square.

A number x is said to be a perfect square if there exists an integer y such that x = y2.

Input
The first line contains a single integer n (1 ≤ n ≤ 1000) — the number of elements in the array.

The second line contains n integers a1, a2, ..., an ( - 106 ≤ ai ≤ 106) — the elements of the array.

It is guaranteed that at least one element of the array is not a perfect square.

Output
Print the largest number in the array which is not a perfect square. It is guaranteed that an answer always exists.
'''
import math 
n = int(input())
rez = 0
arr = [int(x) for x in input().split(' ')]
for a in arr:
    if(a<=0):
        continue
    num = math.sqrt(a)
    if not (num.is_integer()):
        if(a>rez):
            rez=a

if(rez==0):
    rez=max([n for n in arr if n<0])
print(rez)