def maxProfit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    profit = 0
    for day in range(1, len(prices)):
        if prices[day] - prices[day - 1] > 0:
            profit += prices[day] - prices[day - 1]
    return profit
