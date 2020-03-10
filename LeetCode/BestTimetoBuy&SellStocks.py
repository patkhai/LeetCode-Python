'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''


#O(n^2), space O(n)
def maxProfit_BruteForce(prices):
    maxProfit = 0 
    for i in range(len(prices)): 
        for j in range(i+1, len(prices)): 
            profit = prices[j] - prices[i]
            if profit > maxProfit: 
                maxProfit = profit 
    return maxProfit 

#O(n)(loop once), space O(1)(2 variable)
def maxProfit(prices): 
    if len(prices) > 0: 
        lowest,profit = prices[0],0
        for i in range(1,len(prices)): 
            if prices[i] < lowest: 
                lowest = prices[i]
            elif ((prices[i] - lowest) > profit): 
                profit = prices[i] - lowest
    else: 
        profit = 0 
    
    return profit  

#O(n) space 0(1)
def maxProfit2(prices): 
    profit,low = 0, float('inf') 
    for curr_price in prices: 
        if curr_price < low: 
            low = curr_price 
        else: 
            profit = max(curr_price-low,profit)
    return profit

p = [7,1,5,3,6,4]
#return 5 since its the maxprofit
print(maxProfit(p)) 
print(maxProfit_BruteForce(p))
print(maxProfit2(p))

''' 
check if there are prices in the list
set the lowest to the first element of the list and initalize profit 
loop through the second element of the list to the end 
    if the curr element of the list is less than the first element of the list,
    set lowest to that 
    if not then, check if the curr element of the list minus the lowest (first ele) is more than
    profit, if so set profit to that
else if there are no prices, return profit 0 since it is the biggest 
return profit 
''' 