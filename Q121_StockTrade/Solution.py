class solution(object):
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price;
            max_profit = max(max_profit, profit)
        return max_profit
prices = [1, 2, 3, 4, 5, 9, -12, 20]
ans = solution().maxProfit(prices)
print ans