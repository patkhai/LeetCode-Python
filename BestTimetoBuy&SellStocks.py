#O(n^2), space O(1)
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