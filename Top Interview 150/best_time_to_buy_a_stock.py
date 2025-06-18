def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update the minimum price so far
        if price < min_price:
            min_price = price
        # Calculate potential profit and update max profit if better
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit