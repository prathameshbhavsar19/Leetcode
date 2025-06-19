def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit

# Test cases
test_cases = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2, 3, 4, 5], 4),
    ([2, 4, 1], 2),
    ([3, 3, 5, 0, 0, 3, 1, 4], 4),
    ([1], 0),  # Only one price
]

# Run tests
for i, (prices, expected) in enumerate(test_cases):
    result = maxProfit(prices)
    print(f"Test case {i+1}: {'✅ Passed' if result == expected else f'❌ Failed (Expected {expected}, Got {result})'}")