'''
You are given array consisting of n integers. Your task is to find the maximum length of an increasing subarray of the given array.

A subarray is the sequence of consecutive elements of the array. Subarray is called increasing if each element of this subarray strictly greater than previous.

Input
The first line contains single positive integer n (1 ≤ n ≤ 105) — the number of integers.

The second line contains n positive integers a1, a2, ..., an (1 ≤ ai ≤ 109).

Output
Print the maximum length of an increasing subarray of the given array.
'''

n = int(input())
arr = [int(x) for x in input().split(' ')]
bestSubarr= 0
subarr = 0 


for i in range(1, n):
    if(arr[i-1] < arr [i]):
        subarr += 1
        #print('ho')
    else:
        #print('he')
        if(subarr>bestSubarr):
            bestSubarr = subarr
        subarr=0          
    if(i==n-1):
        #print('hi')
        if(subarr>bestSubarr):
            bestSubarr = subarr



print(bestSubarr+1)