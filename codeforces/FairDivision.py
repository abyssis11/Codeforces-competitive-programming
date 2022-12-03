'''
Alice and Bob received n candies from their parents. Each candy weighs either 1 gram or 2 grams. Now they want to divide all candies among themselves fairly so that the total weight of Alice's candies is equal to the total weight of Bob's candies.

Check if they can do that.

Note that candies are not allowed to be cut in half.

Input
The first line contains one integer t (1≤t≤104) — the number of test cases. Then t test cases follow.

The first line of each test case contains an integer n (1≤n≤100) — the number of candies that Alice and Bob received.

The next line contains n integers a1,a2,…,an — the weights of the candies. The weight of each candy is either 1 or 2.

It is guaranteed that the sum of n over all test cases does not exceed 105.

Output
For each test case, output on a separate line:

"YES", if all candies can be divided into two sets with the same weight;
"NO" otherwise.
You can output "YES" and "NO" in any case (for example, the strings yEs, yes, Yes and YES will be recognized as positive).
'''

t = int(input())
tests = [False]*t
for i in range(t):
    #test = []
    n = int(input())
    sum1=0
    sum2=0
    test = [int(x) for x in input().split(' ')]
    for tes in test: 
        if(tes==1):
            sum1+=1
        else:
            sum2+=1
    if sum1 != 0 and sum2 !=0 and ((sum2 % 2== 0 and sum1 % 2 == 0) or (sum2 % 2 != 0 and sum1 % 2 ==0)):
        tests[i]=True
    elif(sum1==0 and sum2 % 2 == 0) or (sum2 ==0 and sum1 % 2==0):
        tests[i]=True
    else: tests[i]=False

for tes in tests:
    if(tes): print('YES')
    else: print('NO')