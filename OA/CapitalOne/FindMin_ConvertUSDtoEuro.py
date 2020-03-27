'''

Given a dollar amount convert it into euro coins and bills 
Convert doolar amount into the least amount of bills and coins

dollar to euro rate is 1.30/$dollar

EURO = [500,200,100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.02,0.01]


Approach: 

Greedy Approach: 
Start from largest possible denomiantion and keep adding denominations 
while remaining value is greater than 0

1. initialize result as empy 
2. find the larget demonimation that is smaller than amount 
3. add found deno to result
subtract value fo found deno from value 
4. if v becomes - then print result 
else repat steps 2 and 3 for new value of v 

input: v = 30 (US dollars)
output: 


''' 
#O(N) or O(dollar_amount)
def convertCurrency(dollar_amount,rate): 
    deno = [0.01,0.02,0.05,0.1,0.25,0.5,1,2,5,10,20,50,100,200,500]

    n = len(deno)

    res = []

    i = n - 1

    dollar_amount /= rate

    while i >= 0: 
        while dollar_amount >= deno[i]:
            dollar_amount -= deno[i] 
            res.append(deno[i])
        i -= 1 
    return res 

print(convertCurrency(30,1.10285))



