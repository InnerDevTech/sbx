def maxProfit(prices):
    n = len(prices)
    buy1 = buy2 = float('-inf')
    sell1 = sell2 = 0
    for i in range(n):
        buy1 = max(buy1, -prices[i])
        sell1 = max(sell1, buy1 + prices[i])
        buy2 = max(buy2, sell1 - prices[i])
        sell2 = max(sell2, buy2 + prices[i])
    return sell2

# Example usage:
prices = [1, 2, 1, 2]
print(maxProfit(prices))  # Output: 120

# Explanation:
# The maximum profit can be achieved by buying at day 0 (price 10), selling at day 3 (price 40),
# buying at day 3 (price 40), and selling at day 6 (price 70).
# The total profit is 40 - 10 + 70 - 40 = 60.